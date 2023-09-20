# imports
# vowels, consonants = generate_letters()
from datetime import datetime
import random

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

def vows_consonsants():

    day = datetime.now().day

    if day == 19:
        vowels = ["A", "O", "U"]
        consonants = ["B", "K", "L", "S"]

    elif day == 20:
        vowels = ["A", "I", "O"]
        consonants = ["B", "D", "T", "S"]

    elif day == 21:
        vowels = ["E", "I", "U"]
        consonants = ["C", "F", "G", "T"]

    elif day == 22:
        vowels = ["I", "O", "U"]
        consonants = ["D", "H", "L", "P"]

    elif day == 23:
        vowels = ["A", "E", "I"]
        consonants = ["B", "D", "K", "R"]



    return vowels, consonants

