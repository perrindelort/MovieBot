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
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import re

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
        
        # Julien
        vectorizer = TfidfVectorizer(stop_words='english')
        synopsis_vectors = vectorizer.fit_transform(self.database[~self.mask]['plot_synopsis_lower'])
        self.similarities = cosine_similarity(synopsis_vectors)
        
        # Hind
        # get all the possible titles in a list
        titles_list = self.database[~self.mask]['title_lower'].unique().tolist()
        self.titles_list = [title for title in titles_list if len(title) != 1]

        # get all the possible genres in a list
        genres = self.database['tags'].str.split(', ').explode().str.strip()
        # removing movie and film because it misleads the detection
        genres = genres.str.replace(r'(\s*)(movie|film)(\s*)', '', regex=True)
        self.genres_list = list(set(genres))
        
# =============================================================================
#         db = self.database.copy()
#         db2 = self.database[~self.mask].copy().reset_index()
#         print(self.database[~self.mask][self.database[~self.mask]['title_lower'] == 'girl vs. monster'].index[0])
#         print(db[~self.mask][db[~self.mask]['title_lower'] == 'girl vs. monster'].index[0])
#         print(db2[db2['title_lower'] == 'girl vs. monster'].index[0])
#         
#         print(self.similarities[db2[db2['title_lower'] == 'girl vs. monster'].index[0]])
# =============================================================================
        
        
       
    def preprocess(self,processed_data_path = ""):
        """
        *** Fonction qui preprocess tout le dataset si nécessaire (mieux à faire si on choisit de pas host un dataset clean sur github)
        *** Input : 
        *** Output : Pas d'output
        """
        # self.database = self.database.drop_duplicates(subset=['title'])
        self.database['plot_synopsis_lower'] = self.database['plot_synopsis'].str.lower()
        self.database['title_lower'] = self.database['title'].str.lower()
        def transform_tags(tag_string):
            return set(tag_string.replace(" ", "").split(','))

        self.database['tags_list'] = self.database['tags'].apply(lambda x: x.split(','))
        self.database['tags_list'] = self.database['tags_list'].apply(lambda tags: tuple(tag.strip() for tag in tags))
        self.database['tags_set'] = self.database['tags'].apply(transform_tags)
        self.database.drop('tags_list', axis = 1)
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
    
    def extract_genres(self,input_string):
        """
        Extracts the genre the bot user asked for and return it
        :param input_string: the message of the bot user
        :return: the genre of the film
        """
        found_genres = []

        # Regex
        input_string_lower = input_string.lower()
        for genre in self.genres_list:
            pattern = r'\b(' + re.escape(genre) + r')\b'
            if re.search(pattern, input_string_lower):
                found_genres.append(genre)

        # fuzzywuzzy
        words = word_tokenize(input_string)
        tagged_tokens = pos_tag(words)
        relevant_words = [word.lower() for word, tag in tagged_tokens if tag.startswith('NN') or tag.startswith('JJ')]
        for word in relevant_words:
            matches = process.extract(word, self.genres_list, scorer=fuzz.partial_ratio)
            for match in matches:
                if match[1] > 85:
                    found_genres.append(match[0])

        if found_genres:
            return True, list(set([x.lower() for x in found_genres]))
        else:
            return False, []
            
    def extract_titles(self, input_string):
        """
        Extracts the title the bot user asked for and return it
        :param input_string: the message of the bot user
        :return: the title of the film
        """
        
        input_string = input_string.lower()
        found_titles = []

        # regex
        for title in self.titles_list:
            pattern = r'\b(' + re.escape(title) + r')\b'
            if re.search(pattern, input_string):
                found_titles.append(title)

        # If many title are detected because of the same word, then delete the small title
        if len(found_titles) > 1:
            found_titles = sorted(found_titles, key=len, reverse=True)
            for i, title in enumerate(found_titles[:-1]):
                for other_title in found_titles[i + 1:]:
                    common_words = set(title.split()) & set(other_title.split())
                    if common_words:
                        found_titles.remove(other_title)
        if found_titles:
            return True, [x.lower() for x in found_titles]
        else:
            return False, []
    
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

        db0=self.database.copy()
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
        print(set_genres)
        # On compte le nombre de tags en commun
        db = self.database.copy()
        db['matching_tags'] = db['tags_set'].apply(lambda tags: len(tags.intersection(set_genres)))
        print(db)
        # On garde uniquement les lignes avec au moins un match  et on drop la colonne créé sur la database
        filtered_database = db[db['matching_tags'] > 0][['title_lower','matching_tags']]
       
        # On randomise les lignes ayant le même nombre de matching tags et on trie par ordre de matching_tags décroissant
        filtered_database['random'] = np.random.rand(filtered_database.shape[0])
       
        # On enlève les films en doubles en gardant celui qui match le mieux les tags 
        # et en breakant les ties avec le random introduit précédemment
        filtered_database = filtered_database.sort_values(by=['matching_tags','random'], ascending = [False,True])
        filtered_database = filtered_database.drop_duplicates(subset = ['title_lower'], keep = 'first')
       
        if filtered_database.shape[0] == 0:
            return False, []
        elif filtered_database.shape[0] <= 5:
            return True, list(filtered_database['title_lower'])
        else:
            print(filtered_database.sort_values(by=['matching_tags'], ascending = False))
            print(filtered_database)
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
        
        db = self.database[~self.mask].copy().reset_index()
        
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
