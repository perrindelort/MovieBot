# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 20:43:13 2024

@author: Antoine

"""
from movie_database import MovieDatabase

def test_julien(database : MovieDatabase):
    liste_movies_1 = ["the haunted", "whale rider", "die hard with a vengeance", "targets", "maid in manhattan"]
    liste_movies_2 = []
    liste_movies_3 = ["nimportequoi", "hbsbksnksd", "uusfksd"]
    liste_movies_4 = ["the haunted", "whale rider", "die hard with a vengeance"]
    liste_movies_5 = ["the haunted", "sdfdsffs", "die hard with a vengeance"]
    liste_movies_6 = ["the haunted", "whale rider", "die hard with a vengeance", "targets", "maid in manhattan","the initiation"]
    
    print("Test 1 :\n" + str(database.retrieve_movies_from_similarity(liste_movies_1)) + "\n")
    print("Test 2 :\n" + str(database.retrieve_movies_from_similarity(liste_movies_2)) + "\n")
    print("Test 3 :\n" + str(database.retrieve_movies_from_similarity(liste_movies_3)) + "\n")
    print("Test 4 :\n" + str(database.retrieve_movies_from_similarity(liste_movies_4)) + "\n")
    print("Test 5 :\n" + str(database.retrieve_movies_from_similarity(liste_movies_5)) + "\n")
    print("Test 6 :\n" + str(database.retrieve_movies_from_similarity(liste_movies_6)) + "\n")
    
def test(database : MovieDatabase):
    test_julien(database)