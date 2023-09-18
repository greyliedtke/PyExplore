# imports
# vowels, consonants = generate_letters()
from datetime import datetime

def vows_consonsants():
    hour = datetime.now().hour
    if hour == 14:
        vowels = ["A", "O", "U"]
        consonants = ["B", "K", "L", "S"]
    else:
        vowels = ["A", "E", "I"]
        consonants = ["L", "M", "P", "T"]

    return vowels, consonants

