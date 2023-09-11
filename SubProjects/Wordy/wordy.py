"""
control page to serve as command center for engine
streamlit run ScaledWiki/SubTesting/SControl/Control.py
"""

# IMPORTS
from nicegui import ui
from funcs import generate_letters, check_word

vowels, consonants = generate_letters()

with ui.expansion("Instructions"):
    ui.markdown(
        """
    - Points:
        - 1 letter = 1 points
        - use all letters = 3 points
    - After 3 submissions, see the best submissions of day
    - See stats of how you did compared to others

        """
    )

word = ui.label("")
words = {}

def del_letter():
    prev_word = word.text
    word.text = prev_word[:-1]

def update_word(letter):
    prev_word = word.text
    word.text = prev_word + letter

def create_b(letter):
    ui.button(letter, on_click=lambda: update_word(letter))


def submit_word():
    resp = check_word(word.text)
    with ui.row():
        with ui.expansion(f"{resp[0]}: {word.text}"):
            ui.markdown(f"{resp[1]}")
    word.text = ""
    words[word.text] = resp[1]
    # add link
    # improve formatting
    

with ui.row():
    for v in vowels:
        create_b(v)
with ui.row():
    for c in consonants:
        create_b(c)

with ui.row():
    ui.button("<-- del", on_click=lambda: del_letter(), color='orange')
    ui.button("Submit", on_click=lambda: submit_word(), color='green')




# running the page
ui.run(title="Wordy", port=2999, binding_refresh_interval=0.5)

# ------------------------------------------------------

"""
other ideas
# with ui.card() as wc:
#     ui.markdown("### Words")
#     word_log = ui.markdown()
    word_log.content = str(words)



"""