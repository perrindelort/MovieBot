# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 17:58:18 2024

@author: Antoine
"""

import pandas as pd
import os


class MovieDatabase():
    def __init__(self,path):
        """
        """
        self.database = pd.read_csv(os.path.join(path, "mpst_full_data.csv"))
        self.preprocess()
       
    def preprocess(self):
        """
        *** Fonction qui preprocess tout le dataset si nécessaire (mieux à faire si on choisit de pas host un dataset clean sur github)
        *** Input : 
        *** Output : Pas d'output
        """
        pass
    
    def retrieve_movies_from_genre(self,genres):
        """
        *** Note : Pour le moment on peut commencer avec un regex pour récupérer les genres, si on veut affiner le truc on peut utiliser un autre réseau
        pour savoir quels genres sont évoqués dans le message 
        (du type 'je veux un film romantique' -> Romance alors qu'avec le Regex il faudrait que l'utilisateur dise 'Romance')
        *** Fonction retournant 5 films dont les genres correspondent à ceux demandé par l'utilisateur 
        et choisit aléatoirement par pondération du score / autre mesure de popularité
        *** Input : genres : Liste des genres voulues par l'utilisateur
        *** Output : Liste comprenant les 5 titres de films en String
        """
        pass
    
    def get_synopsis(self,movie):
        """
        *** Fonction retournant le synopsis d'un film
        *** Input : movie : String du titre du film
        *** Output : String du synopsis du film
        """
        pass
    
    def get_multiple_synopses(self, movies_list):
        """
        *** Fonction retournant un dictionnaire comprenant en clé les titres des films et en valeurs leur synopsis
        *** Input : movies_list : Liste des titres des films
        *** Output : Dictionnaires {"titre" : "synopsis"}
        """
        output = {}
        for movie in movies_list:
            output[movie] = self.get_synopsis(movie)
        return output
    
    def retrieve_movies_from_similarity(self):
        """
        *** Fonction retournant 5 films "proches" d'un ou plusieurs films spécifiés par l'utilisateurs
        *** Input :
        *** Output : 
        """
        pass
