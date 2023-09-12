"""
control page to serve as command center for engine
streamlit run ScaledWiki/SubTesting/SControl/Control.py
"""

# IMPORTS
from nicegui import ui, app
from funcs import generate_letters, check_word
from wordbank import vowels, consonants

# parse guessed words and link to google
def guess_parser(guess_dict:dict):
    # file to convert guess dictionary into markdown list of items
    md_string = ""
    for k, v in guess_dict.items():
        md_string += f"\n- [{k}](https://www.google.com/search?q={k})"
        try:
            v = dict(v)
            for nva, nvav in v.items():
                md_string += f"\n       - {nva}: {nvav[0]}"
        except:
            continue
    return md_string


@ui.page('/')
def index():

    
    words = {}

    def del_letter():
        prev_word = word.text
        word.text = prev_word[:-1]

    def update_word(letter):
        prev_word = word.text
        word.text = prev_word + letter

    def create_b(letter):
        ui.button(letter, on_click=lambda: update_word(letter))

    def submit_word(typed_word:str):
        typed_word = typed_word.lower()
        resp = check_word(typed_word)

        words[typed_word] = resp[1]
        guesses = app.storage.user.get("guesses", {})
        guesses[typed_word] = resp[1]
        app.storage.user["guesses"] = guesses

        # clear responses
        word.text = ""

        # update page

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

    app.storage.user["info"] = app.storage.user.get("info", 0)
    user = app.storage.user["info"]
    ui.markdown(f"{user}")

    with ui.card():
        # game card
        word = ui.label("")
        with ui.row():
            for v in vowels:
                create_b(v)
        with ui.row():
            for c in consonants:
                create_b(c)

        with ui.row():
            ui.button("<-- del", on_click=lambda: del_letter(), color='orange')
            ui.button("Submit", on_click=lambda: submit_word(word.text), color='green')

    guess_md = guess_parser(app.storage.user.get("guesses", {}))

    with ui.card():
        ui.markdown("### Guesses")
        ui.markdown(f"""
                    {guess_md}
                    """)

# running the page
ui.run(title="Wordy", port=2999, binding_refresh_interval=0.5, storage_secret="xxx")

# ------------------------------------------------------