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
        
def test_maxime(database : MovieDatabase):
    
    def test_is_retrieve_movie_from_genre_correct(input_text):
        pass
    
    def test_is_retrieve_movie_from_genre_optimized_correct(input_text):
        pass
    
    
    
    def test_1(input = []): #ne doit rien renvoyer
        print("input: ",input)
        try:
            success,ids,titles = database.retrieve_movies_from_genre(input)

            # Si votre fonction a réussi le test
            if not success and ids==[] and titles==[]:
                # Je m'arrangerai pour que ça soit en vert dans le cmd
                print(f"ids : {ids}")
                print(f"titles : {titles}")
                return True
            # Si votre fonction a raté le test
            else:
                # Je m'arrangerai pour que ça soit en rouge dans le cmd
                print(f"ids : {ids}")
                print(f"titles : {titles}")
                return False

        # Si il y a eu une quelconque erreur lors de l'exécution du code
        except:
            return False
    
    def test_1_optimized(input = []): #ne doit rien renvoyer
        print("input: ",input)
        try:
            success,ids,titles = database.retrieve_movies_from_genre_optimized(input)

            # Si votre fonction a réussi le test
            if not success and ids==[] and titles==[]:
                # Je m'arrangerai pour que ça soit en vert dans le cmd
                print(f"ids : {ids}")
                print(f"titles : {titles}")
                return True
            # Si votre fonction a raté le test
            else:
                # Je m'arrangerai pour que ça soit en rouge dans le cmd
                print(f"ids : {ids}")
                print(f"titles : {titles}")
                return False

        # Si il y a eu une quelconque erreur lors de l'exécution du code
        except:
            return False
    
    def test_2(input = ["chien","chat"]): #ne doit rien renvoyer
        print("input: ",input)
        try:
            success,ids,titles = database.retrieve_movies_from_genre(input)

            # Si votre fonction a réussi le test
            if not success and ids==[] and titles==[]:
                # Je m'arrangerai pour que ça soit en vert dans le cmd
                print(f"ids : {ids}")
                print(f"titles : {titles}")
                return True
            # Si votre fonction a raté le test
            else:
                # Je m'arrangerai pour que ça soit en rouge dans le cmd
                print(f"ids : {ids}")
                print(f"titles : {titles}")
                return False

        # Si il y a eu une quelconque erreur lors de l'exécution du code
        except:
            return False
    
    def test_2_optimized(input = ["chien","chat"]): #ne doit rien renvoyer
        print("input: ",input)
        try:
            success,ids,titles = database.retrieve_movies_from_genre_optimized(input)

            # Si votre fonction a réussi le test
            if not success and ids==[] and titles==[]:
                # Je m'arrangerai pour que ça soit en vert dans le cmd
                print(f"ids : {ids}")
                print(f"titles : {titles}")
                return True
            # Si votre fonction a raté le test
            else:
                # Je m'arrangerai pour que ça soit en rouge dans le cmd
                print(f"ids : {ids}")
                print(f"titles : {titles}")
                return False

        # Si il y a eu une quelconque erreur lors de l'exécution du code
        except:
            return False
        
    
    def test_3(input = ["horror","good versus evil","insanity","cult","gothic"]): # exactement 5 films ont ces 5 tags
        print("input: ",input)
        try:
            success,ids,titles = database.retrieve_movies_from_genre(input)
            # Si votre fonction a réussi le test
            check_ids='tt0103874' in ids and 'tt0095294' in ids and 'tt0101917' in ids and 'tt0273517'in ids and 'tt0120681' in ids and len(ids)==5
            check_titles='dracula' in titles and 'hellbound: hellraiser ii' in titles and "freddy's dead: the final nightmare" in titles and 'darkness'in titles and 'from hell' in titles and len(titles)==5
            if success and check_ids and check_titles:
                # Je m'arrangerai pour que ça soit en vert dans le cmd
                print(f"ids : {ids}")
                print(f"titles : {titles}")
                return True
            # Si votre fonction a raté le test
            else:
                # Je m'arrangerai pour que ça soit en rouge dans le cmd
                print(f"ids : {ids}")
                print(f"titles : {titles}")
                return False

        # Si il y a eu une quelconque erreur lors de l'exécution du code
        except:
            return False

    def test_3_optimized(input = ["horror","good versus evil","insanity","cult","gothic"]): # exactement 5 films ont ces 5 tags
        print("input: ",input)
        try:
            success,ids,titles = database.retrieve_movies_from_genre_optimized(input)
            # Si votre fonction a réussi le test
            check_ids='tt0103874' in ids and 'tt0095294' in ids and 'tt0101917' in ids and 'tt0273517'in ids and 'tt0120681' in ids and len(ids)==5
            check_titles='dracula' in titles and 'hellbound: hellraiser ii' in titles and "freddy's dead: the final nightmare" in titles and 'darkness'in titles and 'from hell' in titles and len(titles)==5
            if success and check_ids and check_titles:
                # Je m'arrangerai pour que ça soit en vert dans le cmd
                print(f"ids : {ids}")
                print(f"titles : {titles}")
                return True
            # Si votre fonction a raté le test
            else:
                # Je m'arrangerai pour que ça soit en rouge dans le cmd
                print(f"ids : {ids}")
                print(f"titles : {titles}")
                return False

        # Si il y a eu une quelconque erreur lors de l'exécution du code
        except:
            return False
        
    def test_4(input = ["good versus evil","insanity","cult","gothic"]): # test qui pourrait contenir plusieurs Draculas (normalement non), à lancer plusieurs fois
        print("input: ",input)
        try:
            success,ids,titles = database.retrieve_movies_from_genre(input)
            # Si votre fonction a réussi le test
            ids_allowed=['tt0233298', 'tt0091474', 'tt0119099', 'tt0103874', 'tt0096895', 'tt0021814', 'tt0216651', 'tt0095294', 'tt0103776', 'tt0113409', 'tt0114194', 'tt0093605', 'tt0246578', 'tt0100260', 'tt0330373', 'tt0106364', 'tt0114825', 'tt0101917', 'tt0468569', 'tt0273517', 'tt0115986', 'tt0353324', 'tt0120681']
            titles_allowed=['batman beyond: return of the joker', 'manhunter', 'fallen', 'batman', 'dracula', 'vampire hunter d: bloodlust', 'hellbound: hellraiser ii', 'batman returns', 'in the mouth of madness', 'the prophecy', 'near dark', 'donnie darko', 'nightbreed', 'harry potter and the goblet of fire', 'batman: mask of the phantasm', 'vampire in brooklyn', "freddy's dead: the final nightmare", 'the dark knight', 'darkness', 'the crow: city of angels', 'the crow: wicked prayer', 'from hell']
            check_ids=ids[0] in ids_allowed and ids[1] in ids_allowed and ids[2] in ids_allowed and ids[3] in ids_allowed and ids[4] in ids_allowed and len(ids)==5
            check_titles=titles[0] in titles_allowed and titles[1] in titles_allowed and titles[2] in titles_allowed and titles[3] in titles_allowed and titles[4] in titles_allowed and len(titles)==5
            unique=[]
            for title in titles:
                if title not in unique:
                    unique.append(title)
            check_uniqueness=(len(unique)==5)
            if success and check_ids and check_titles and check_uniqueness:
                # Je m'arrangerai pour que ça soit en vert dans le cmd
                print(f"ids : {ids}")
                print(f"titles : {titles}")
                return True
            # Si votre fonction a raté le test
            else:
                # Je m'arrangerai pour que ça soit en rouge dans le cmd
                print(f"ids : {ids}")
                print(f"titles : {titles}")
                return False

        # Si il y a eu une quelconque erreur lors de l'exécution du code
        except:
            return False

    def test_4_optimized(input = ["good versus evil","insanity","cult","gothic"]): # test qui pourrait contenir plusieurs Draculas (normalement non), à lancer plusieurs fois
        print("input: ",input)
        try:
            success,ids,titles = database.retrieve_movies_from_genre_optimized(input)
            # Si votre fonction a réussi le test
            ids_allowed=['tt0233298', 'tt0091474', 'tt0119099', 'tt0103874', 'tt0096895', 'tt0021814', 'tt0216651', 'tt0095294', 'tt0103776', 'tt0113409', 'tt0114194', 'tt0093605', 'tt0246578', 'tt0100260', 'tt0330373', 'tt0106364', 'tt0114825', 'tt0101917', 'tt0468569', 'tt0273517', 'tt0115986', 'tt0353324', 'tt0120681']
            titles_allowed=['batman beyond: return of the joker', 'manhunter', 'fallen', 'batman', 'dracula', 'vampire hunter d: bloodlust', 'hellbound: hellraiser ii', 'batman returns', 'in the mouth of madness', 'the prophecy', 'near dark', 'donnie darko', 'nightbreed', 'harry potter and the goblet of fire', 'batman: mask of the phantasm', 'vampire in brooklyn', "freddy's dead: the final nightmare", 'the dark knight', 'darkness', 'the crow: city of angels', 'the crow: wicked prayer', 'from hell']
            check_ids=ids[0] in ids_allowed and ids[1] in ids_allowed and ids[2] in ids_allowed and ids[3] in ids_allowed and ids[4] in ids_allowed and len(ids)==5
            check_titles=titles[0] in titles_allowed and titles[1] in titles_allowed and titles[2] in titles_allowed and titles[3] in titles_allowed and titles[4] in titles_allowed and len(titles)==5
            unique=[]
            for title in titles:
                if title not in unique:
                    unique.append(title)
            check_uniqueness=(len(unique)==5)
            if success and check_ids and check_titles and check_uniqueness:
                # Je m'arrangerai pour que ça soit en vert dans le cmd
                print(f"ids : {ids}")
                print(f"titles : {titles}")
                return True
            # Si votre fonction a raté le test
            else:
                # Je m'arrangerai pour que ça soit en rouge dans le cmd
                print(f"ids : {ids}")
                print(f"titles : {titles}")
                return False

        # Si il y a eu une quelconque erreur lors de l'exécution du code
        except:
            return False

    def test_5(input = ["horror","good versus evil","insanity","cult","gothic","romantic"]): # test contenant un titre obligatoire (dracula) et 4 autres random parmi un pool
        print("input: ",input)
        try:
            success,ids,titles = database.retrieve_movies_from_genre(input)
            # Si votre fonction a réussi le test
            ids_allowed=['tt0103874', 'tt0102926', 'tt0076786', 'tt0216651', 'tt0095294', 'tt0093605', 'tt0401792', 'tt1213856', 'tt0100260', 'tt0120082', 'tt0106364', 'tt0457430', 'tt0114825', 'tt0101917', 'tt0054215', 'tt0074285', 'tt0273517', 'tt0115986', 'tt0353324', 'tt0120681']
            titles_allowed=['dracula', 'the silence of the lambs', 'suspiria', 'vampire hunter d: bloodlust', 'hellbound: hellraiser ii', 'near dark', 'sin city', 'du saram-yida', 'nightbreed', 'scream 2', 'batman: mask of the phantasm', 'el laberinto del fauno', 'vampire in brooklyn', "freddy's dead: the final nightmare", 'psycho', 'carrie', 'darkness', 'the crow: city of angels', 'the crow: wicked prayer', 'from hell']
            check_ids='tt0103874' in ids and ids[1] in ids_allowed and ids[2] in ids_allowed and ids[3] in ids_allowed and ids[4] in ids_allowed and len(ids)==5
            check_titles='dracula' in titles and titles[1] in titles_allowed and titles[2] in titles_allowed and titles[3] in titles_allowed and titles[4] in titles_allowed and len(titles)==5
            unique=[]
            for title in titles:
                if title not in unique:
                    unique.append(title)
            check_uniqueness=(len(unique)==5)
            if success and check_ids and check_titles and check_uniqueness:
                # Je m'arrangerai pour que ça soit en vert dans le cmd
                print(f"ids : {ids}")
                print(f"titles : {titles}")
                return True
            # Si votre fonction a raté le test
            else:
                # Je m'arrangerai pour que ça soit en rouge dans le cmd
                print(f"ids : {ids}")
                print(f"titles : {titles}")
                return False

        # Si il y a eu une quelconque erreur lors de l'exécution du code
        except:
            return False
        
    def test_5_optimized(input = ["horror","good versus evil","insanity","cult","gothic","romantic"]): # test contenant un titre obligatoire (dracula) et 4 autres random parmi un pool
        print("input: ",input)
        try:
            success,ids,titles = database.retrieve_movies_from_genre_optimized(input)
            # Si votre fonction a réussi le test
            ids_allowed=['tt0103874', 'tt0102926', 'tt0076786', 'tt0216651', 'tt0095294', 'tt0093605', 'tt0401792', 'tt1213856', 'tt0100260', 'tt0120082', 'tt0106364', 'tt0457430', 'tt0114825', 'tt0101917', 'tt0054215', 'tt0074285', 'tt0273517', 'tt0115986', 'tt0353324', 'tt0120681']
            titles_allowed=['dracula', 'the silence of the lambs', 'suspiria', 'vampire hunter d: bloodlust', 'hellbound: hellraiser ii', 'near dark', 'sin city', 'du saram-yida', 'nightbreed', 'scream 2', 'batman: mask of the phantasm', 'el laberinto del fauno', 'vampire in brooklyn', "freddy's dead: the final nightmare", 'psycho', 'carrie', 'darkness', 'the crow: city of angels', 'the crow: wicked prayer', 'from hell']
            check_ids='tt0103874' in ids and ids[1] in ids_allowed and ids[2] in ids_allowed and ids[3] in ids_allowed and ids[4] in ids_allowed and len(ids)==5
            check_titles='dracula' in titles and titles[1] in titles_allowed and titles[2] in titles_allowed and titles[3] in titles_allowed and titles[4] in titles_allowed and len(titles)==5
            unique=[]
            for title in titles:
                if title not in unique:
                    unique.append(title)
            check_uniqueness=(len(unique)==5)
            if success and check_ids and check_titles and check_uniqueness:
                # Je m'arrangerai pour que ça soit en vert dans le cmd
                print(f"ids : {ids}")
                print(f"titles : {titles}")
                return True
            # Si votre fonction a raté le test
            else:
                # Je m'arrangerai pour que ça soit en rouge dans le cmd
                print(f"ids : {ids}")
                print(f"titles : {titles}")
                return False

        # Si il y a eu une quelconque erreur lors de l'exécution du code
        except:
            return False

    # Je compterai le nombre de tests réussis...
    
    print("tests 1\n")
    test_1()
    test_1_optimized()
    print("\n")

    print("tests 2\n")
    test_2()
    test_2_optimized()
    print("\n")

    print("tests 3\n") 
    test_3()
    test_3_optimized()
    print("\n")

    print("tests 4\n") # a executer plusieurs fois idéalement
    test_4()
    test_4_optimized()
    print("\n")

    print("tests 5\n") # a executer plusieurs fois idéalement
    test_5()
    test_5_optimized()


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
