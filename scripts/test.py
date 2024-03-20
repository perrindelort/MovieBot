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
                                                  "Ta mère en string",
                                                  " ééé e g؛@", 
                                                  "",
                                                  "Hello I am busy today",
                                                  "ذخرس؛@"
                                                  ],
                                   'expected_output' : [['plot twist', 'horror'],
                                                        ['romantic'],
                                                        ['melodrama','dramatic'],
                                                        ['entertaining','dramatic','western','clever','cult'],
                                                        [],
                                                        [],
                                                        [],
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
        
def test_maxime(database : MovieDatabase):
    
    def test_is_retrieve_movie_from_genre_correct_1(input_text, expected_output_titles, expected_output_ids):
        try:
            success, titles, ids = database.retrieve_movies_from_genre(input_text)
            same_titles = set(titles) == set(expected_output_titles) and len(titles) == len(expected_output_titles)
            same_ids = set(ids) == set(expected_output_ids) and len(ids) == len(expected_output_ids)
            if not success and same_titles and same_ids:
                return True, titles, ids
            else:
                return False, titles, ids
        except Exception as e:
            print(f"Error: {e}")
            return False, None, None
    
    def test_is_retrieve_movie_from_genre_optimized_correct_1(input_text, expected_output_titles, expected_output_ids):
        try:
            success, titles, ids = database.retrieve_movies_from_genre_optimized(input_text)
            same_titles = set(titles) == set(expected_output_titles) and len(titles) == len(expected_output_titles)
            same_ids = set(ids) == set(expected_output_ids) and len(ids) == len(expected_output_ids)
            if not success and same_titles and same_ids:
                return True, titles, ids
            else:
                return False, titles, ids
        except Exception as e:
            print(f"Error: {e}")
            return False, None, None
        
    def test_is_retrieve_movie_from_genre_correct_2(input_text, allowed_output_titles, allowed_output_ids):
        try:
            success, titles, ids = database.retrieve_movies_from_genre(input_text)
            if not success and len(set(titles).intersection(set(allowed_output_titles))) == 5 and len(set(ids).intersection(set(allowed_output_ids))) == 5:
                return True, titles, ids
            else:
                return False, titles, ids
        except Exception as e:
            print(f"Error: {e}")
            return False, None, None
    
    def test_is_retrieve_movie_from_genre_optimized_correct_2(input_text, allowed_output_titles, allowed_output_ids):
        try:
            success, titles, ids = database.retrieve_movies_from_genre_optimized(input_text)
            if not success and len(set(titles).intersection(set(allowed_output_titles))) == 5 and len(set(ids).intersection(set(allowed_output_ids))) == 5:
                return True, titles, ids
            else:
                return False, titles, ids
        except Exception as e:
            print(f"Error: {e}")
            return False, None, None
    
    is_retrieve_movie_from_genre_correct_1 = {'input_text' : [[],
                                                            ["chien","chat"],
                                                            ["horror","good versus evil","insanity","cult","gothic"]
                                                            ],
                                            'expected_output_titles' : [[],
                                                                        [],
                                                                        ["dracula","hellbound: hellraiser ii","freddy's dead: the final nightmare","darkness","from hell"]
                                                                        ],
                                            'expected_output_ids' : [[],
                                                                     [],
                                                                     ["tt0103874","tt0095294","tt0101917","tt0273517","tt0120681"]
                                                                     ]
                                            }
    
    functions_1 = [test_is_retrieve_movie_from_genre_correct_1,test_is_retrieve_movie_from_genre_optimized_correct_1]
    
    is_retrieve_movie_from_genre_correct_2 = {'input_text' : [["good versus evil","insanity","cult","gothic"],
                                                              ["horror","good versus evil","insanity","cult","gothic","romantic"]
                                                            ],
                                            'allowed_output_titles' : [['batman beyond: return of the joker', 'manhunter', 'fallen', 'batman', 'dracula', 'vampire hunter d: bloodlust', 'hellbound: hellraiser ii', 'batman returns', 'in the mouth of madness', 'the prophecy', 'near dark', 'donnie darko', 'nightbreed', 'harry potter and the goblet of fire', 'batman: mask of the phantasm', 'vampire in brooklyn', "freddy's dead: the final nightmare", 'the dark knight', 'darkness', 'the crow: city of angels', 'the crow: wicked prayer', 'from hell'],
                                                                        ['dracula', 'the silence of the lambs', 'suspiria', 'vampire hunter d: bloodlust', 'hellbound: hellraiser ii', 'near dark', 'sin city', 'du saram-yida', 'nightbreed', 'scream 2', 'batman: mask of the phantasm', 'el laberinto del fauno', 'vampire in brooklyn', "freddy's dead: the final nightmare", 'psycho', 'carrie', 'darkness', 'the crow: city of angels', 'the crow: wicked prayer', 'from hell']
                                                                        ],
                                            'allowed_output_ids' : [['tt0233298', 'tt0091474', 'tt0119099', 'tt0103874', 'tt0096895', 'tt0021814', 'tt0216651', 'tt0095294', 'tt0103776', 'tt0113409', 'tt0114194', 'tt0093605', 'tt0246578', 'tt0100260', 'tt0330373', 'tt0106364', 'tt0114825', 'tt0101917', 'tt0468569', 'tt0273517', 'tt0115986', 'tt0353324', 'tt0120681'],
                                                                     ['tt0103874', 'tt0102926', 'tt0076786', 'tt0216651', 'tt0095294', 'tt0093605', 'tt0401792', 'tt1213856', 'tt0100260', 'tt0120082', 'tt0106364', 'tt0457430', 'tt0114825', 'tt0101917', 'tt0054215', 'tt0074285', 'tt0273517', 'tt0115986', 'tt0353324', 'tt0120681']
                                                                     ]
                                            }
    
    functions_2 = [test_is_retrieve_movie_from_genre_correct_2,test_is_retrieve_movie_from_genre_optimized_correct_2]
    
    test_number = 1
    
    for idx,fn in enumerate(functions_1):
        for input_text, expected_output_titles, expected_output_ids in zip(is_retrieve_movie_from_genre_correct_1['input_text'],is_retrieve_movie_from_genre_correct_1['expected_output_titles'],is_retrieve_movie_from_genre_correct_1['expected_output_ids']):
            passed, output_titles, output_ids = fn(input_text,expected_output_titles, expected_output_ids)
            if passed:
                print(colored(f"Test {test_number} : passed", 'green'))
            else:
                func_type = "unoptimized" if idx == 0 else "optimized"
                print(colored(f"Test {test_number} : failed \n    Fonction : {func_type} \n    Input : {input_text} \n    Output : {output_titles} \n              {output_ids} \n    Expected output : {expected_output_titles}  \n                    : {expected_output_ids}  \n",'red'))
            test_number += 1
    
    for idx,fn in enumerate(functions_2):
        for input_text, allowed_output_titles, allowed_output_ids in zip(is_retrieve_movie_from_genre_correct_2['input_text'],is_retrieve_movie_from_genre_correct_2['allowed_output_titles'],is_retrieve_movie_from_genre_correct_2['allowed_output_ids']):
            passed, output_titles, output_ids = fn(input_text,expected_output_titles, expected_output_ids)
            if passed:
                print(colored(f"Test {test_number} : passed", 'green'))
            else:
                func_type = "unoptimized" if idx == 0 else "optimized"
                print(colored(f"Test {test_number} : failed \n    Fonction : {func_type} \n    Input : {input_text} \n    Output : {output_titles} \n              {output_ids} \n    Allowed output : {allowed_output_titles}  \n                   : {allowed_output_ids}  \n",'red'))
            test_number += 1
 
        

def test(database : MovieDatabase):
    n_dashes = 100
    print("\n Début des tests \n" + "-"*n_dashes)
    print("                             TEST DE HIND                             ")
    test_hind(database)
    print("                            TEST DE JULIEN                            ")
    test_julien(database)
    print("                            TEST DE MAXIME                            ")
    test_maxime(database)
    print("-"*n_dashes)
