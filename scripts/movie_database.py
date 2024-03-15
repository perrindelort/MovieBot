# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 17:58:18 2024

@author: Antoine
Branch Julien
"""

import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieDatabase():
    def __init__(self,path, / ,bool_preprocess = False):
        """
        """
        data_path = os.path.join(path, "mpst_full_data_test.csv")
        processed_data_path = os.path.join(path, "mpst_processed_data_test.csv")
        if os.path.exists(processed_data_path):
            if bool_preprocess == False:
                self.database = pd.read_csv(processed_data_path)
            else:
                self.database = pd.read_csv(data_path)
                self.preprocess(processed_data_path)
              
        else:
            # Gérer le cas de téléchargement du dataset depuis Kaggle
            if os.path.exists(data_path) == False:
                #print("A")
                #api = KaggleApi()
                #api.dataset_download_files('cryptexcode/mpst-movie-plot-synopses-with-tags', path=data_path)
                pass
                
            self.database = pd.read_csv(data_path)
            self.preprocess(processed_data_path)
            
        vectorizer = TfidfVectorizer(stop_words='english')
        synopsis_vectors = vectorizer.fit_transform(self.database['plot_synopsis_lower'])
        self.similarities = cosine_similarity(synopsis_vectors)


       
    def preprocess(self,processed_data_path):
        """
        *** Fonction qui preprocess tout le dataset si nécessaire (mieux à faire si on choisit de pas host un dataset clean sur github)
        *** Input : 
        *** Output : Pas d'output
        """
        self.database = self.database.drop_duplicates(subset=['title'])
        self.database['plot_synopsis_lower'] = self.database['plot_synopsis'].str.lower()
        self.database['title_lower'] = self.database['title'].str.lower()
        self.database.to_csv(processed_data_path)
    
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
    
    def retrieve_movies_from_similarity(self, list_movies) :
        """
        Inputs : - df après preprocessing
                 - liste de film déjà passés en minuscules
                 
        Output : - liste de titres de 5 films 

                        - cas 1 : aucun film valide en entrée : random 5 films
                            
                        - cas 2 : au moins 5 films en entrée valides : 
                            
                            chaque film le plus proche tour à tour des 5 premiers films valides de la liste
                            
                        - cas 3 : entre 1 et 4 films en entrée valides :
                            
                            chaque film le plus proche tour à tour des films valides de la liste 
                            puis on recommence au début de la liste jusqu'à avoir 5 films différents à proposer                   
        """
        list_return = []
        liste_index = [] 
        length = 0
        
        # Tri des films valides
        for i in list_movies :                   
            if i in self.database['title_lower'].tolist():
                length += 1
            else :
                list_movies.remove(i)
        
        # Cas 1
        if length == 0 :                                  
            # list_return = self.database['title'].sample(n=5, replace=False).tolist()
            return False, []
        # Cas 2 et 3
        else :                                        
            while len(list_return) < 5 :        
                for titre in list_movies:              
                    index_movie = self.database[self.database['title_lower'] == titre].index[0]
                    similarities_to_movie = self.similarities[index_movie]
                    most_similar_index = similarities_to_movie.argmax()
                    count = 0
                    while (most_similar_index == index_movie) or (most_similar_index in liste_index) :
                        count += 1
                        most_similar_index = similarities_to_movie.argsort()[-1-count]
                    most_similar_movie_title = self.database.loc[most_similar_index, 'title']
                    liste_index.append(most_similar_index)
                    list_return.append(most_similar_movie_title)
                    if len(list_return) == 5:
                        break    
        return True, list_return    
