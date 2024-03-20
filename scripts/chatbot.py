# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:09:16 2024

@author: Antoine
"""

import gradio as gr


import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, StoppingCriteria, StoppingCriteriaList, TextIteratorStreamer
from threading import Thread

from utils import *
from movie_database import MovieDatabase

class HelloChatBot():
    def __init__(self):
        self.demo = gr.Interface(fn=self.greet, inputs="text", outputs="text")

    def greet(self,name):
        return "Hello " + name + "!"
    
    def launch(self):
        self.demo.launch()   

class BinaryChatBot():
    def __init__(self):
        self.demo = gr.ChatInterface(self.alternatingly_agree)
        
    def alternatingly_agree(self,message, history):
        if len(history) % 2 == 0:
            return f"Yes, I do think that '{message}'"
        else:
            return "I don't think so"
        
    def launch(self):
        self.demo.launch()

class MovieRecommandationChatBot():
    def __init__(self, language = "ENG"):
        self.language = language
        
        self.demo = gr.ChatInterface(fn=self.chat, 
                                     title = CHATBOT_TITLE, 
                                     chatbot = gr.Chatbot(value=[[None, CHATBOT_INITIAL_MESSAGE[self.language]]]),
                                     examples = list(FIXED_COMMANDS[self.language].keys()))
        
        
        
        
        self.state = 0 
        """
        0 -> Attente d'une consigne de l'utilisateur
        1 -> Attente des genres du film que l'utilisateur recherche
        2 -> Attente des films qui se rapprochent du film que l'utilisateur recherche
        """
        self.substate = 0
        """
        0 -> Demande plus de précisions à l'utilisateur
        1 -> Répond à l'utilisateur
        """
    
    def set_database(self,database : MovieDatabase):
        self.database = database
    
    def update_state(self,message):
        try:
            self.state = FIXED_COMMANDS[self.language][message]
            return True
        except:
            return False
        
    def reset_states(self):
        self.state = 0
        self.substate = 0
        
    def update_substate(self):
        self.substate += 1 
        self.substate %= 2
    
    def chat(self,message,history):
        
        print(f"En recevant le message {message} l'état du bot est le suivant : \n    state : {self.state} \n    substate : {self.substate}")
        # Retour au menu
        if message == INV_FIXED_COMMANDS[self.language][0]:
            self.reset_states()
            return FIXED_MESSAGES[self.language]["RETOUR MENU"]
        
        if self.state == 0:
            
            # On reset les états (notamment substate)
            self.reset_states()
            
            # On update l'état (state) du bot en fonction de l'input utilisateur
            is_state_updated = self.update_state(message)
            
            # Si l'état n'est pas update (input incorrect), on redemande à l'utilisateur jusqu'à obtenir un input correct
            while is_state_updated == False:
                return  FIXED_MESSAGES[self.language]["INPUT INCORRECT"]
        
        if self.state != 0:
            print(f"self.state : {self.state}")
            
            # On retourne à l'utilisateur 5 films en fonction de genres qu'il demande
            if self.state == 1:
                
                # On demande des genres de film à l'utilisateur
                if self.substate == 0:
                    self.update_substate()
                    return FIXED_MESSAGES[self.language]["DEMANDER GENRES"]
                
                # On retourne des suggestions de films à l'utilisateur
                elif self.substate == 1:
                    extracted, list_genres = self.database.extract_genres(message)
                    #extracted, list_genres = True, ['romantic']
                    print(extracted, list_genres)
                    if extracted == True:
                        # retrieved, retrieved_movies, retrieved_ids = self.database.retrieve_movies_from_genre(list_genres)
                        retrieved, retrieved_movies, retrieved_ids = self.database.retrieve_movies_from_genre_optimized(list_genres)
                        print(f"list_genres : {list_genres}")
                        print(retrieved_movies)
                        if retrieved == True:
                            self.reset_states()
                            return FIXED_MESSAGES[self.language]['REPONSE GENRES'] + " ".join([genre for genre in list_genres]) + " ! \n    - " + "\n    - ".join(retrieved_movies)
    
                        
                        # On n'a trouvé aucun film correspondant aux genres demandés par l'utilisateur dans la database
                        # OU l'utilisateur n'a pas soumis de genres / on n'a pas compris les genres soumis
                        else:
                            # On ne met pas à jour le state
                            # On redemande des genres à l'utilisateur
                            return FIXED_MESSAGES[self.language]['GENRES INCONNUS']
                    else:
                        return FIXED_MESSAGES[self.language]['GENRES INCONNUS']
                else:
                    raise ValueError(f"Valeur incorrecte : self.substate = {self.substate}")
                    
            # On retourne à l'utilisateur 5 films se rapprochant des synopsis de films qu'il a déjà vu
            elif self.state == 2:
                
                # On demande des titres de films à l'utilisateur
                if self.substate == 0:
                    self.update_substate()
                    return FIXED_MESSAGES[self.language]["DEMANDER FILMS"]
                
                # On retourne des suggestions de films à l'utilisateur
                elif self.substate == 1:
                    extracted, list_movies = self.database.extract_titles(message)
                    # extracted, list_movies = True, ['girl vs. monster']
                    print(extracted, list_movies)
                    if extracted == True:
                        retrieved, retrieved_movies = self.database.retrieve_movies_from_similarity(list_movies)
                        if retrieved == True:
                            self.reset_states()
                            return FIXED_MESSAGES[self.language]['REPONSE FILMS'] + "\n    - ".join(retrieved_movies)
                        
                        # On n'a trouvé aucun film évoqué par l'utilisateur dans la database
                        else:
                            # On ne met pas à jour le state
                            # On redemande des films à l'utilisateur
                            return FIXED_MESSAGES[self.language]["FILMS INCONNUS"]
                    else:
                        return FIXED_MESSAGES[self.language]["FILMS INCONNUS"]
                else:
                    raise ValueError(f"Valeur incorrecte : self.substate = {self.substate}")
                    
            # ValueError
            else:
                print(self.state)
                raise ValueError(f"Valeur incorrecte : self.state = {self.state}")
        
            
    def launch(self):
        self.demo.launch()

class LLMChatBot():
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("togethercomputer/RedPajama-INCITE-Chat-3B-v1")
        self.model = AutoModelForCausalLM.from_pretrained("togethercomputer/RedPajama-INCITE-Chat-3B-v1", torch_dtype=torch.float16)
        self.model.to('cuda:0')
        self.demo = gr.ChatInterface(self.predict)
    
    def predict(self,message, history):
        history_transformer_format = history + [[message, ""]]
        stop = StopOnTokens()

        messages = "".join(["".join(["\n<human>:"+item[0], "\n<bot>:"+item[1]])
                    for item in history_transformer_format])

        model_inputs = self.tokenizer([messages], return_tensors="pt").to("cuda")
        streamer = TextIteratorStreamer(self.tokenizer, timeout=10., skip_prompt=True, skip_special_tokens=True)
        generate_kwargs = dict(
            model_inputs,
            streamer=streamer,
            max_new_tokens=1024,
            do_sample=True,
            top_p=0.95,
            top_k=1000,
            temperature=1.0,
            num_beams=1,
            stopping_criteria=StoppingCriteriaList([stop])
            )
        t = Thread(target=self.model.generate, kwargs=generate_kwargs)
        t.start()

        partial_message = ""
        for new_token in streamer:
            if new_token != '<':
                partial_message += new_token
                yield partial_message
    
    def launch(self):
        self.demo.launch()

class StopOnTokens(StoppingCriteria):
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
        stop_ids = [29, 0]
        for stop_id in stop_ids:
            if input_ids[0][-1] == stop_id:
                return True
        return False


def create_chatbot(chatbot_type):
    if chatbot_type == "HelloChatBot":
        return HelloChatBot()
    elif chatbot_type == "BinaryChatBot":
        return BinaryChatBot()
    elif chatbot_type == "LLMChatBot":
        return LLMChatBot()
    elif chatbot_type == "MovieRecommandationChatBot":
        return MovieRecommandationChatBot()
    else:
        raise ValueError(f"{chatbot_type} n'est pas un argument valable pour créer un chabot")

