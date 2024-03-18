# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 11:32:48 2024

@author: Antoine
"""

import argparse
from utils import CHATBOT_TITLE
class ChatBotArgumentParser(argparse.ArgumentParser):
    def __init__(self):
        super().__init__(description="coucou")
        self.add_argument("-c","--chatbot",type=str, 
                          dest = "chatbot",
                          choices = ["HelloChatBot","BinaryChatBot","LLMChatBot"],
                          default = "MovieRecommandationChatBot",
                          help="Avec quel chatbot voulez-vous interagir ? Les choix possibles sont : \n - HelloChatBot \n - BinaryChatBot")
        
        self.add_argument("-t","--train",
                          dest = "train",
                          action = "store_true",
                          default = False,
                          help = "Voulez-vous re-train les modèles ?")
        
        self.add_argument("-p","--preprocess",
                          dest = "bool_preprocess",
                          action = "store_true",
                          default = False,
                          help = "Voulez-vous relancer le preprocess des données ?")
        
        self.add_argument("--test",
                          dest = "test",
                          action = "store_true",
                          default = False,
                          help = "Voulez-vous voir le résultats des tests ? ?")
        
        self.add_argument("-l", "--language",
                          dest = "language",
                          choices = ["ENG","FRA"],
                          default = "ENG",
                          help = f"Quelle langue doit parler / comprendre {CHATBOT_TITLE} ?")
        