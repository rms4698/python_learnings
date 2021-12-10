import json
import os
from difflib import get_close_matches

""" Set the directory name """
dirname = os.path.dirname(__file__)
input_file_path = os.path.join(dirname, "data.json")
input_file_path = r"D:\ModernLab\Learning\Python\App1_Thesaurus\Input files\data.json"

word_dic = {}
with open(input_file_path, mode="r") as f:
    word_dic = json.load(f)

""" Created a dic to hold all the key's lower case to find """
word_dic_small = {}
for i in word_dic:
    word_dic_small[i.lower()] = i

""" Return an common error message """
def word_doesnt_exist_error():
    return "Hmm, Looks like the word doesn't exist! Double check the word, Buddy!"


""" Get the word & return the meaning """
def translate(given_word):
    given_word_small = given_word.lower()
    if given_word_small in word_dic_small:
        """ Word is available """
        return(word_dic[word_dic_small[given_word_small]])
    else:
        """ Word is not available; Check for the closest matches"""
        try:
            closest_match = get_close_matches(given_word_small, word_dic_small.keys())[0]
        except IndexError:
            return word_doesnt_exist_error()
        
        "Got the closest word"
        check_with_user = input("Did you mean {} instead of {}, Enter Y if yes, N if no: ".format(closest_match, given_word))
        if check_with_user.lower() == "y":
            """ User confirmed the word """
            return(word_dic[word_dic_small[closest_match]])
        elif check_with_user.lower() == "n":
            """ Word doesn't exist """
            return word_doesnt_exist_error()
        else:
            return "Input is invalid"

while True:
    """ Get the input from user """
    given_word = input("Enter a word : ")

    """ Get the meaning & print it """
    meaning = translate(given_word)
    if type(meaning) == list:
        print("\n".join(meaning))
    else:
        print(meaning)

    yn = input("Do want to continue y/n?")

    if yn == "n":
        break

