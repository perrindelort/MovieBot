# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 17:04:51 2024

@author: Antoine
"""
import os

from movie_database import MovieDatabase
from chatbot import create_chatbot
from custom_arg_parser import ChatBotArgumentParser

if __name__ == "__main__":
    parser = ChatBotArgumentParser()
    args = parser.parse_args()
    print(args)
    PATH = os.path.dirname(os.path.abspath(__file__))
    #print(PATH)
    #print(os.path.join(PATH, "..", "datasets"))
    database = MovieDatabase(path = os.path.join(PATH, "..", "datasets"), 
                             bool_preprocess = args.bool_preprocess)
    chatbot = create_chatbot(args.chatbot)
    chatbot.set_database(database)
    
    if args.test:
        test(database)
    
    chatbot.launch()