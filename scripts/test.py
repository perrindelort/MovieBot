# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 20:43:13 2024

@author: Antoine
"""
from movie_database import MovieDatabase
from termcolor import colored


def test_julien(database : MovieDatabase, detailed_passed_test = False):
    def test_is_retrieve_movies_from_similarity_correct(input_text, expected_output):
        try:
            passed, output = database.retrieve_movies_from_similarity(input_text)
            # Si votre fonction a réussi le test
            return output == expected_output, output
        except Exception as e:
            print(e)
            return False, None
        
        
    is_retrieve_movies_from_similarity_correct = {'input_text' : [["the haunted", "whale rider", "die hard with a vengeance", "targets", "maid in manhattan"],
                                                                  [],
                                                                  ["nimportequoi", "hbsbksnksd", "uusfksd"],
                                                                  ["the haunted", "whale rider", "die hard with a vengeance"],
                                                                  ["the haunted", "sdfdsffs", "die hard with a vengeance"],
                                                                  ["the haunted", "whale rider", "die hard with a vengeance", "targets", "maid in manhattan","the initiation"]
                                                                  ],
                                                  'expected_output' : [['Little Miss Sunshine', 'Insidious', 'Le clan des Siciliens', 'One Day', 'One Dark Night'],
                                                                       [],
                                                                       [],
                                                                       ['Little Miss Sunshine', 'Insidious', 'Le clan des Siciliens', 'Porky Chops', 'Artemis Fowl'],
                                                                       ['Little Miss Sunshine', 'Le clan des Siciliens', 'Porky Chops', 'Dangerous Liaisons', 'Duplex'],
                                                                       ['Little Miss Sunshine', 'Insidious', 'Le clan des Siciliens', 'One Day', 'One Dark Night']
                                                                       ]
                                                  }

    test_number = 1 
    for input_text,expected_output in zip(is_retrieve_movies_from_similarity_correct['input_text'],is_retrieve_movies_from_similarity_correct['expected_output']):
        passed, output = test_is_retrieve_movies_from_similarity_correct(input_text,expected_output)
        if passed:
            if detailed_passed_test:
                print(colored(f"Test {test_number} : failed \n    Input : {input_text} \n    Output : {output} \n    Expected output : {expected_output} \n",'green'))
            else:
                print(colored(f"Test {test_number} : passed", 'green'))
        else:
            print(colored(f"Test {test_number} : failed \n    Input : {input_text} \n    Output : {output} \n    Expected output : {expected_output} \n",'red'))
        test_number += 1
    
        
        
def test_hind(database : MovieDatabase, detailed_passed_test = False):
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
            if detailed_passed_test:
                print(colored(f"Test {test_number} : passed \n    Input : {input_text} \n    Output : {output} \n    Expected output : {expected_output} \n",'green'))
            else:
                print(colored(f"Test {test_number} : passed", 'green'))
        else:
            print(colored(f"Test {test_number} : failed \n    Input : {input_text} \n    Output : {output} \n    Expected output : {expected_output} \n",'red'))
        test_number += 1
        
    for input_text,expected_output in zip(is_extraction_title_correct['input_text'],is_extraction_title_correct['expected_output']):
        passed, output = test_is_extraction_movie_correct(input_text,expected_output)
        if passed:
            if detailed_passed_test:
                print(colored(f"Test {test_number} : passed \n    Input : {input_text} \n    Output : {output} \n    Expected output : {expected_output} \n",'green'))
            else:
                print(colored(f"Test {test_number} : passed", 'green'))
        else:
            print(colored(f"Test {test_number} : failed \n    Input : {input_text} \n    Output : {output} \n    Expected output : {expected_output} \n",'red'))
        test_number += 1
        
def test_maxime(database : MovieDatabase, detailed_passed_test = False):
    
    def test_is_retrieve_movie_from_genre_correct_1(input_text, expected_output_titles, expected_output_ids):
        try:
            success, titles, ids = database.retrieve_movies_from_genre(input_text)
            same_titles = set(titles) == set(expected_output_titles) and len(titles) == len(expected_output_titles)
            same_ids = set(ids) == set(expected_output_ids) and len(ids) == len(expected_output_ids)
            if same_titles and same_ids:
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
            if same_titles and same_ids:
                return True, titles, ids
            else:
                return False, titles, ids
        except Exception as e:
            print(f"Error: {e}")
            return False, None, None
        
    def test_is_retrieve_movie_from_genre_correct_2(input_text, allowed_output_titles, allowed_output_ids):
        try:
            success, titles, ids = database.retrieve_movies_from_genre(input_text)
            if len(set(titles).intersection(set(allowed_output_titles))) == 5 and len(set(ids).intersection(set(allowed_output_ids))) == 5:
                return True, titles, ids
            else:
                return False, titles, ids
        except Exception as e:
            print(f"Error: {e}")
            return False, None, None
    
    def test_is_retrieve_movie_from_genre_optimized_correct_2(input_text, allowed_output_titles, allowed_output_ids):
        try:
            success, titles, ids = database.retrieve_movies_from_genre_optimized(input_text)
            if len(set(titles).intersection(set(allowed_output_titles))) == 5 and len(set(ids).intersection(set(allowed_output_ids))) == 5:
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
                                                                        ['Dracula', 'Hellbound: Hellraiser II', "Freddy's Dead: The Final Nightmare", 'Darkness', 'From Hell']
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
                                            'allowed_output_titles' : [['Batman Beyond: Return of the Joker', 'Manhunter', 'Fallen', 'Dracula', 'Batman', 'Dracula', 'Vampire Hunter D: Bloodlust', 'Hellbound: Hellraiser II', 'Batman Returns', 'In the Mouth of Madness', 'The Prophecy', 'Near Dark', 'Donnie Darko', 'Nightbreed', 'Harry Potter and the Goblet of Fire', 'Batman: Mask of the Phantasm', 'Vampire in Brooklyn', "Freddy's Dead: The Final Nightmare", 'The Dark Knight', 'Darkness', 'The Crow: City of Angels', 'The Crow: Wicked Prayer', 'From Hell'],
                                                                        ['Dracula', 'The Silence of the Lambs', 'Suspiria', 'Vampire Hunter D: Bloodlust', 'Hellbound: Hellraiser II', 'Near Dark', 'Sin City', 'Du saram-yida', 'Nightbreed', 'Scream 2', 'Batman: Mask of the Phantasm', 'El laberinto del fauno', 'Vampire in Brooklyn', "Freddy's Dead: The Final Nightmare", 'Psycho', 'Carrie', 'Darkness', 'The Crow: City of Angels', 'The Crow: Wicked Prayer', 'From Hell']
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
                if detailed_passed_test:
                    func_type = "unoptimized" if idx == 0 else "optimized"
                    print(colored(f"Test {test_number} : passed \n    Fonction : {func_type} \n    Input : {input_text} \n    Output : {output_titles} \n              {output_ids} \n    Expected output : {expected_output_titles}  \n                    : {expected_output_ids}  \n",'green'))
                else:
                    print(colored(f"Test {test_number} : passed", 'green'))
            else:
                func_type = "unoptimized" if idx == 0 else "optimized"
                print(colored(f"Test {test_number} : failed \n    Fonction : {func_type} \n    Input : {input_text} \n    Output : {output_titles} \n              {output_ids} \n    Expected output : {expected_output_titles}  \n                    : {expected_output_ids}  \n",'red'))
            test_number += 1
    
    for idx,fn in enumerate(functions_2):
        for input_text, allowed_output_titles, allowed_output_ids in zip(is_retrieve_movie_from_genre_correct_2['input_text'],is_retrieve_movie_from_genre_correct_2['allowed_output_titles'],is_retrieve_movie_from_genre_correct_2['allowed_output_ids']):
            passed, output_titles, output_ids = fn(input_text,allowed_output_titles, allowed_output_ids)
            if passed:
                if detailed_passed_test:
                    func_type = "unoptimized" if idx == 0 else "optimized"
                    print(colored(f"Test {test_number} : passed \n    Fonction : {func_type} \n    Input : {input_text} \n    Output : {output_titles} \n             {output_ids} \n    Allowed output : {allowed_output_titles}  \n                     {allowed_output_ids}  \n",'green'))
                else:
                    print(colored(f"Test {test_number} : passed", 'green'))
            else:
                func_type = "unoptimized" if idx == 0 else "optimized"
                print(colored(f"Test {test_number} : failed \n    Fonction : {func_type} \n    Input : {input_text} \n    Output : {output_titles} \n             {output_ids} \n    Allowed output : {allowed_output_titles}  \n                     {allowed_output_ids}  \n",'red'))
            test_number += 1
 
        

def test(database : MovieDatabase, detailed_passed_test = False):
    dashes = "-"*100
    spaces = " " * 30
    print("\n Début des tests \n")
    print(dashes)
    print(spaces + "TEST DE HIND" + spaces)
    test_hind(database, detailed_passed_test = detailed_passed_test)
    print(dashes)
    print("                            TEST DE JULIEN                            ")
    test_julien(database, detailed_passed_test = detailed_passed_test)
    print(dashes)
    print("                            TEST DE MAXIME                            ")
    test_maxime(database, detailed_passed_test = detailed_passed_test)
    print(dashes)
