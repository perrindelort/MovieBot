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
import random
import numpy as np

class MovieDatabase():
    def __init__(self,path,bool_preprocess = False):
        """
        """
        data_path = os.path.join(path, "mpst_full_data.csv")
        """
        processed_data_path = os.path.join(path, "mpst_processed_data.csv")
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
        """
        
        self.database = pd.read_csv(data_path)
        self.preprocess()
        self.mask = self.database.duplicated(subset = ['title'])

        vectorizer = TfidfVectorizer(stop_words='english')
        synopsis_vectors = vectorizer.fit_transform(self.database[~self.mask]['plot_synopsis_lower'])
        self.similarities = cosine_similarity(synopsis_vectors)


       
    def preprocess(self,processed_data_path = ""):
        """
        *** Fonction qui preprocess tout le dataset si nécessaire (mieux à faire si on choisit de pas host un dataset clean sur github)
        *** Input : 
        *** Output : Pas d'output
        """
        # self.database = self.database.drop_duplicates(subset=['title'])
        self.database['plot_synopsis_lower'] = self.database['plot_synopsis'].str.lower()
        self.database['title_lower'] = self.database['title'].str.lower()
        self.database['tags_list'] = self.database['tags'].apply(lambda x: x.split(','))
        # self.database.to_csv(processed_data_path)
    
    def unique_title(self,films_ids):
        unique=[]
        titles=[]
        db0=self.database
        db=db0.set_index("imdb_id")
        for id in films_ids:
            title=db["title"][id]
            if title not in titles:
                titles.append(title)
                unique.append(id)
        return unique
    
    
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

        db0=self.database
        db=db0.set_index("imdb_id")
        dict_films={} #dictionnaire comptant le nombre n de matchs avec les tags. clés: id, contenu: n

        # les lignes suivantes génèrent le dictionnaire
        for id_film in db.index:
            for genre in genres:
                if genre in db["tags"][id_film]:
                    if id_film not in dict_films.keys():
                        dict_films[id_film]=1
                    else:
                        dict_films[id_film]+=1

        # on crée une liste rangée par valeur de n décroissante
        sorted_by_matching = dict(sorted(dict_films.items(), key=lambda x:(x[1]), reverse=True))
        sorted_list=list(sorted_by_matching.keys())
        
        
        # Si y'a pas de match : return False
        if len(sorted_list) == 0:
            return False, []
        
        # si cette liste est de taille inférieure à 5 (5 films ou moins matchent avec au moins un tag) on la renvoie directement en ne
        # gardant qu'un film par titre
        if len(sorted_list)<=5:
            return True, self.unique_title(sorted_list)
        
        # sinon on sélectionne au fur et à mesure les candidats qui matchent le mieux jusqu'à remplir les 5 places. On part du meilleur
        # score N, et on compte le nombre de films qui ont N tags en commun avec la liste d'entrée. Si ce nombre est supérieur à 5, on
        # en tire 5 au hasard, sinon on les ajoute à la liste des places disponibles, et on répète l'opération avec le deuxième meilleur
        # score et les places restantes à attribuer.
        
        suggested=[]
        i,j=0,0
        while len(suggested)<5 and j<len(sorted_list):
            best_film=sorted_list[i]
            best_matching=sorted_by_matching[best_film]
            current_film=sorted_list[j]
            current_matching=sorted_by_matching[current_film]
            remaining=5-len(suggested)
            while j<len(sorted_list) and current_matching==best_matching:
                j+=1
                current_film=sorted_list[j]
                current_matching=sorted_by_matching[current_film]

            list_with_doubles=suggested+sorted_list[i:j]


            list_without_doubles=self.unique_title(list_with_doubles)
            candidates=list_without_doubles[i:]

            candidates_titles=[]
            for id in list_with_doubles:
                candidates_titles.append(db["title"][id])
            #print(candidates_titles)

            n_candidates=len(candidates)
            if n_candidates<=remaining:
                suggested=suggested+candidates
                i=j
            else:
                suggested=suggested+random.sample(candidates,remaining)
        suggested_titles=[]
        for id in suggested:
            suggested_titles.append(db["title"][id])
            
        #return suggested,suggested_titles
        return True, suggested_titles
    
    
    def retrieve_movies_from_genre_optimized(self,genres):
        
        set_genres = set(genres)
        
        # On compte le nombre de tags en commun
        self.database['matching_tags'] = self.database['tags_list'].apply(lambda x : len(set(x).intersection(set_genres)))
        
        # On garde uniquement les lignes avec au moins un match  et on drop la colonne créé sur la database
        filtered_database = self.database[self.database['matching_tags'] > 0][['title_lower','matching_tags']]
        self.database.drop('matching_tags')
        
        # On randomise les lignes ayant le même nombre de matching tags et on trie par ordre de matching_tags décroissant
        for value in filtered_database['matching_tags'].unique():
            idx = filtered_database.index[filtered_database['matching_tags'] == value]
            np.random.shuffle(idx)
            filtered_database.loc[idx, 'random'] = np.random.rand(len(idx))
        filtered_database = filtered_database.sort_values(by=['matching_tags','random'], ascending = [False,True]).drop(columns='random')
        
        # On enlève les films en doubles en gardant celui qui match le mieux les tags 
        # et en breakant les ties avec le random introduit précédemment
        filtered_database = filtered_database.drop_duplicates(subset = ['title_lower'], keep = 'first')
        
        if filtered_database[0].shape == 0:
            return False, []
        elif filtered_database[0].shape <= 5:
            return True, list(filtered_database['title_lower'])
        else:
            return True,list(filtered_database['title_lower'])[:5]
    
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
        
        db = self.database[~self.mask]
        
        # Tri des films valides
        for i in list_movies :                   
            if i in db['title_lower'].tolist():
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
                    index_movie = db[db['title_lower'] == titre].index[0]
                    similarities_to_movie = self.similarities[index_movie]
                    most_similar_index = similarities_to_movie.argmax()
                    count = 0
                    while (most_similar_index == index_movie) or (most_similar_index in liste_index) :
                        count += 1
                        most_similar_index = similarities_to_movie.argsort()[-1-count]
                    most_similar_movie_title = db.loc[most_similar_index, 'title']
                    liste_index.append(most_similar_index)
                    list_return.append(most_similar_movie_title)
                    if len(list_return) == 5:
                        break    
        return True, list_return    
