# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:59:49 2024

@author: Antoine
"""

CHATBOT_TITLE = "MovieBot"
CHATBOT_INITIAL_MESSAGE = f"Bonjour je suis {CHATBOT_TITLE}, votre assistant pour décider quoi regarder ce soir !"

FIXED_COMMANDS = {"Je souhaite revenir au menu" : 0,
                  "Je souhaite que l'on me conseille un film par genre" : 1,
                  "Je souhaite que l'on me conseille un film selon mes préférences" : 2}

FIXED_MESSAGES = {'INPUT INCORRECT' : "Je n'ai pas compris votre demande, entrez l'une des commandes suivantes : \n    - "+'\n    - '.join(FIXED_COMMANDS.keys()),
                  'RETOUR ETAT 0' : "J'espère avoir répondu à votre demande ! \n Si vous avez d'autres questions à me poser n'hésitez pas ! :)",
                  'DEMANDER GENRES' : "Quel genre de film voulez-vous voir ce soir ?",
                  'DEMANDER FILMS' : "Quels films avez vous-vu et/ou apprécié ?"}
