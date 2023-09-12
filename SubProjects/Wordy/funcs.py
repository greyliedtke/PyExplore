# imports
import random
from PyDictionary import PyDictionary
dictionary=PyDictionary()

# Define a list of vowels and consonants
vowels = ['A', 'E', 'I', 'O', 'U']
consonants = [chr(x) for x in range(ord('A'), ord('Z') + 1) if chr(x) not in vowels]


def generate_letters():
    # Generate 2 random vowels and 4 random consonants
    pv = random.sample(vowels, k=3) 
    pc = random.sample(consonants, k=4)

    pv = sorted(pv)
    pc = sorted(pc)

    return pv, pc


# score the words created
# each letter is 1 word. using all letters is 3 points
def check_word(word):
    points = 0 

    points = len(word)

    u_letters = set(word)
    if u_letters == 6:
        points+=3

    def_dict = dictionary.meaning(word)
    if def_dict is None:
        points = 0
        print(f"NOT A WORD: {word}")
    
    return points, def_dict



