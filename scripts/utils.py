# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:59:49 2024

@author: Antoine
"""
import random

CHATBOT_TITLE = "MovieBot"

CHATBOT_INITIAL_MESSAGE = {"ENG" : f"Hello I am {CHATBOT_TITLE}, your assistant created to help you decide what to watch tonight !",
                            "FRA" : f"Bonjour je suis {CHATBOT_TITLE}, votre assistant pour décider quoi regarder ce soir !"}



FIXED_COMMANDS = {"ENG" : {"I'd like to go back to the menu selection" : 0,
                           "I'd like to get a movie recommendation given some genres" : 1,
                           "I'd like to get a movie recommendation from movies I like" : 2},
                  "FRA" : {"Je souhaite revenir au menu" : 0,
                           "Je souhaite que l'on me conseille un film par genre" : 1,
                           "Je souhaite que l'on me conseille un film selon mes préférences" : 2}}

INV_FIXED_COMMANDS = {"ENG" : {v: k for k, v in FIXED_COMMANDS["ENG"].items()},
                      "FRA" : {v: k for k, v in FIXED_COMMANDS["FRA"].items()}
                      }

FIXED_MESSAGES = {"ENG" : {'INPUT INCORRECT' : "I did not understand what you asked for, enter one of the following demand : \n    - " + '\n    - '.join(FIXED_COMMANDS["ENG"].keys()),
                           'RETOUR ETAT 0' : "I hope I've been of some help ! \n If you have another question feel free to ask ! :)",
                           'DEMANDER GENRES' : "What kind of movie do you want to watch tonight ?",
                           'DEMANDER FILMS' : "Give me somes movies that you've seen and like !",
                           'FILMS INCONNUS' : "It seems like I don't know any movie you've told me. \n Can you submit more movies in order for me to help you ?",
                           'GENRES INCONNUS' : "It seems like I don't know any of the genre you mentionned. \n Can you submit more genres in order for me to help you ?",
                           'RETOUR MENU' :  "You are back to the menu ! Enter one of the following demand \n    - " + '\n    - '.join(list(FIXED_COMMANDS["ENG"].keys())[1:]),
                           'REPONSE GENRES' : "Here are movies that best correspond to the tags  ",
                           'REPONSE FILMS' : "Here are my movies recommendation ! \n    - " }
,
                  "FRA" : {'INPUT INCORRECT' : "Je n'ai pas compris votre demande, entrez l'une des commandes suivantes : \n    - " + '\n    - '.join(FIXED_COMMANDS["FRA"].keys()),
                           'RETOUR ETAT 0' : "J'espère avoir répondu à votre demande ! \n Si vous avez d'autres questions à me poser n'hésitez pas ! :)",
                           'DEMANDER GENRES' : "Quel genre de film voulez-vous voir ce soir ?",
                           'DEMANDER FILMS' : "Quels films avez vous-vu et/ou apprécié ?",
                           'FILMS INCONNUS' : "Il semblerait que je ne connaisse aucun des films que vous avez évoqué. \n Pouvez-vous me soumettre de nouveaux titres de films afin que je puisse vous conseiller",
                           'GENRES INCONNUS' : "Il semblerait que je ne connaisse aucun des genres que vous avez évoqué. \n Pouvez-vous me soumettre de nouveaux genres de films afin que je puisse vous conseiller",
                           'RETOUR MENU' :  "Vous êtes de retour au menu ! Entrez l'une des commandes suivantes \n    - " + '\n    - '.join(list(FIXED_COMMANDS["FRA"].keys())[1:]),
                           'REPONSE GENRES' : "Voici les films que je vous propose qui correspondent le mieux aux tags ",
                           'REPONSE FILMS' : "Voici les films que je vous propose ! \n    - " }
}

def randomly_alter_string(string):
    altered_string = list(string)
    length = len(string)

    # Randomly remove a character
    if random.random() < 0.2:
        index_to_remove = random.randint(0, length - 1)
        del altered_string[index_to_remove]

    # Randomly insert a space
    if random.random() < 0.2:
        index_to_insert = random.randint(0, length - 1)
        altered_string.insert(index_to_insert, ' ')

    # Randomly duplicate a character
    if random.random() < 0.2:
        index_to_duplicate = random.randint(0, length - 1)
        altered_string.insert(index_to_duplicate, altered_string[index_to_duplicate])

    # Randomly replace a character
    if random.random() < 0.2:
        index_to_replace = random.randint(0, length - 1)
        altered_string[index_to_replace] = chr(random.randint(ord('a'), ord('z')))

    # Randomly change case of a character
    if random.random() < 0.2:
        index_to_change_case = random.randint(0, length - 1)
        if altered_string[index_to_change_case].isalpha():
            altered_string[index_to_change_case] = altered_string[index_to_change_case].swapcase()

    return ''.join(altered_string)