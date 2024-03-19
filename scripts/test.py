# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 20:43:13 2024

@author: Antoine
"""
from movie_database import MovieDatabase


# def test_julien(database : MovieDatabase):
#     liste_movies_1 = ["the haunted", "whale rider", "die hard with a vengeance", "targets", "maid in manhattan"]
#     liste_movies_2 = []
#     liste_movies_3 = ["nimportequoi", "hbsbksnksd", "uusfksd"]
#     liste_movies_4 = ["the haunted", "whale rider", "die hard with a vengeance"]
#     liste_movies_5 = ["the haunted", "sdfdsffs", "die hard with a vengeance"]
#     liste_movies_6 = ["the haunted", "whale rider", "die hard with a vengeance", "targets", "maid in manhattan","the initiation"]
#
#     test_list = [liste_movies_1,
#                  liste_movies_2,
#                  liste_movies_3,
#                  liste_movies_4,
#                  liste_movies_5,
#                  liste_movies_6]
#
#     for idx, liste_movies in enumerate(test_list):
#         print(f"Test {idx} : \n    Input : {liste_movies} ")
#         print(f"    Output : {database.retrieve_movies_from_similarity(liste_movies)} \n")
#
# # =============================================================================
# #     print("Test 1 :\n" + str(database.retrieve_movies_from_similarity(liste_movies_1)) + "\n")
# #     print("Test 2 :\n" + str(database.retrieve_movies_from_similarity(liste_movies_2)) + "\n")
# #     print("Test 3 :\n" + str(database.retrieve_movies_from_similarity(liste_movies_3)) + "\n")
# #     print("Test 4 :\n" + str(database.retrieve_movies_from_similarity(liste_movies_4)) + "\n")
# #     print("Test 5 :\n" + str(database.retrieve_movies_from_similarity(liste_movies_5)) + "\n")
# #     print("Test 6 :\n" + str(database.retrieve_movies_from_similarity(liste_movies_6)) + "\n")
# # =============================================================================

class Test_extract_genres:
    @staticmethod
    def test_0(input_text="I want a plot twist film or horror"):
        try:
            output = sorted(database.extract_genres(input_text)[1], key=lambda x: len(x), reverse=True)
            expected_output = ['plot twist', 'horror']
            return output == expected_output
        except Exception as e:
            print(f"Error: {e}")
            return False

    @staticmethod
    def test_1(input_text="rommantic film is my favourite"):
        try:
            output = sorted(database.extract_genres(input_text)[1], key=lambda x: len(x), reverse=True)
            expected_output = ['romantic']
            return output == expected_output
        except Exception as e:
            print(f"Error: {e}")
            return False

    @staticmethod
    def test_2(input_text="I love drama melodrama and dramatic movies the best"):
        try:
            output = sorted(database.extract_genres(input_text)[1], key=lambda x: len(x), reverse=True)
            expected_output = ['melodrama','dramatic']
            return output == expected_output
        except Exception as e:
            print(f"Error: {e}")
            return False

    @staticmethod
    def test_3(input_text="'dramatic','cult','western','clever','entertaining'"):
        try:
            output = sorted(database.extract_genres(input_text)[1], key=lambda x: len(x), reverse=True)
            expected_output = ['entertaining','dramatic','western','clever','cult']
            return output == expected_output
        except Exception as e:
            print(f"Error: {e}")
            return False


class Test_extract_titles:
    @staticmethod
    def test_0(input_text="I want a film similar to skeleton crew"):
        try:
            output = sorted(database.extract_titles(input_text)[1], key=lambda x: len(x), reverse=True)
            expected_output = ['skeleton crew']
            return output == expected_output
        except Exception as e:
            print(f"Error: {e}")
            return False

    @staticmethod
    def test_1(input_text="girl vs. monster is my best film"):
        try:
            output = sorted(database.extract_titles(input_text)[1], key=lambda x: len(x), reverse=True)
            expected_output = ['girl vs. monster']
            return output == expected_output
        except Exception as e:
            print(f"Error: {e}")
            return False

    @staticmethod
    def test_2(input_text="MONSTER"):
        try:
            output = sorted(database.extract_titles(input_text)[1], key=lambda x: len(x), reverse=True)
            expected_output = ['monster']
            return output == expected_output
        except Exception as e:
            print(f"Error: {e}")
            return False


if __name__ == "__main__":
    database = MovieDatabase(r'C:\Users\hindf\Documents\3eme annee TAF Dasci\8_NLP\projet\chatbot_\datasets')

    results_extract_genres = []
    results_extract_genres.append(Test_extract_genres.test_0())
    results_extract_genres.append(Test_extract_genres.test_1())
    results_extract_genres.append(Test_extract_genres.test_2())
    results_extract_genres.append(Test_extract_genres.test_3())

    print("Test de extract_genres ")
    for i, result in enumerate(results_extract_genres):
        print(f"Test {i} {'Passed' if result else 'Failed'}")

    results_extract_titles = []
    results_extract_titles.append(Test_extract_titles.test_0())
    results_extract_titles.append(Test_extract_titles.test_1())
    results_extract_titles.append(Test_extract_titles.test_2())

    print("Test de extract_titles ")
    for i, result in enumerate(results_extract_titles):
        print(f"Test {i} {'Passed' if result else 'Failed'}")
