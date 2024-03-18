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
    
    test_list = [liste_movies_1,
                 liste_movies_2,
                 liste_movies_3,
                 liste_movies_4,
                 liste_movies_5,
                 liste_movies_6]
    
    for idx, liste_movies in enumerate(test_list):
        print(f"Test {idx} : \n    Input : {liste_movies} ")
        print(f"    Output : {database.retrieve_movies_from_similarity(liste_movies)} \n")
    
# =============================================================================
#     print("Test 1 :\n" + str(database.retrieve_movies_from_similarity(liste_movies_1)) + "\n")
#     print("Test 2 :\n" + str(database.retrieve_movies_from_similarity(liste_movies_2)) + "\n")
#     print("Test 3 :\n" + str(database.retrieve_movies_from_similarity(liste_movies_3)) + "\n")
#     print("Test 4 :\n" + str(database.retrieve_movies_from_similarity(liste_movies_4)) + "\n")
#     print("Test 5 :\n" + str(database.retrieve_movies_from_similarity(liste_movies_5)) + "\n")
#     print("Test 6 :\n" + str(database.retrieve_movies_from_similarity(liste_movies_6)) + "\n")
# =============================================================================
    
def test_hind(database : MovieDatabase):
    # test genre intent
    print("**********Test finding genre**********")
    genre_strings = [
        "I want a suspens film or horror",
        "rommantic film is my favourite",
        "A film about drama",
        "I want a comedye movie",
        "action",
        "mystery",
        'I love the haunted !',
        "the haunted,whale rider,die hard with a vengeance,targets,maid in manhattan,the initiation",
        "drama",
        " I love drama and crime !",
        "I love drama drama melodrama and dramatic movies the best",
        "'dramatic','action','cult','western','clever','entertaining'",
        "I love dramatic movies that are cult, entertaining with a lot of action. If they're western of cult movies I like them even more !!!"
    ]
    
    for idx,input_string in enumerate(genre_strings):
        print(f"Test {idx} : \n    Input : {input_string}")
        extracted, genres = database.extract_genres(input_string)
        print(f"    Output : {genres} \n")


    # test title intent
    print("**********Test finding title**********")
    title_strings = [
        "I want a film similar to skeleton crew",
        "girl vs. monster is my best film and I also like monster",
        "le plaisir",
        "monster"
    ]
    
    for idx,input_string in enumerate(title_strings):
        print(f"Test {idx} : \n    Input : {input_string} ")
        extracted, titles = database.extract_titles(input_string)
        print(f"    Output : {titles} \n")
    
    
def test(database : MovieDatabase):
    n_dashes = 100
    print("\n Début des tests \n" + "-"*n_dashes)
    print("                             TEST DE HIND                             ")
    test_hind(database)
    print("                            TEST DE JULIEN                            ")
    test_julien(database)
    print("-"*n_dashes)