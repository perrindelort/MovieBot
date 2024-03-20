# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 20:43:13 2024

@author: Antoine
"""
from movie_database import MovieDatabase
from termcolor import colored


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
        
        
def test_hind(database : MovieDatabase):
    def test_is_extraction_genre_correct(input_text, expected_output):
        try:
            output = sorted(database.extract_genres(input_text)[1], key=lambda x: len(x), reverse=True)
            return output == expected_output, output
        except Exception as e:
            print(f"Error: {e}")
            return False, None
        
    def test_is_extraction_movie_correct(input_text, expected_input):
        try:
            output = sorted(database.extract_titles(input_text)[1], key=lambda x: len(x), reverse=True)
            return output == expected_output, output
        except Exception as e:
            print(f"Error: {e}")
            return False, None
            
    
    is_extraction_genre_correct = {'input_text' : ["I want a plot twist film or horror",
                                                   "rommantic film is my favourite",
                                                  "I love drama melodrama and dramatic movies the best",
                                                  "'dramatic','cult','western','clever','entertaining'",
                                                  "Ta mère en string"
                                                  ],
                                   'expected_output' : [['plot twist', 'horror'],
                                                        ['romantic'],
                                                        ['melodrama','dramatic'],
                                                        ['entertaining','dramatic','western','clever','cult'],
                                                        []
                                                        ]
                                   }
    
    is_extraction_title_correct = {'input_text' : ["I want a film similar to skeleton crew",
                                                   "girl vs. monster is my best film",
                                                   "MONSTER",
                                                   ],
                                   'expected_output' : [['skeleton crew'],
                                                        ['girl vs. monster'],
                                                        ['monster']
                                                        ]
       
                                   }
    
    test_number = 1 
    for input_text,expected_output in zip(is_extraction_genre_correct['input_text'],is_extraction_genre_correct['expected_output']):
        passed, output = test_is_extraction_genre_correct(input_text,expected_output)
        if passed:
            print(colored(f"Test {test_number} : passed", 'green'))
        else:
            print(colored(f"Test {test_number} : failed \n    Input : {input_text} \n    Output : {output} \n    Expected output : {expected_output} \n",'red'))
        test_number += 1
        
    for input_text,expected_output in zip(is_extraction_title_correct['input_text'],is_extraction_title_correct['expected_output']):
        passed, output = test_is_extraction_movie_correct(input_text,expected_output)
        if passed:
            print(colored(f"Test {test_number} : passed", 'green'))
        else:
            print(colored(f"Test {test_number} : failed \n    Input : {input_text} \n    Output : {output} \n    Expected output : {expected_output} \n",'red'))
        test_number += 1
        


def test(database : MovieDatabase):
    n_dashes = 100
    print("\n Début des tests \n" + "-"*n_dashes)
    print("                             TEST DE HIND                             ")
    test_hind(database)
    print("                            TEST DE JULIEN                            ")
    test_julien(database)
    print("                            TEST DE MAXIME                            ")
    # test_maxime(database)
    print("-"*n_dashes)
