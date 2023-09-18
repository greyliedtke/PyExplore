"""

"""

# IMPORTS
from nicegui import ui, app
from funcs import generate_letters, check_word, guess_parser, guess_inc
from wordbank import vows_consonsants
from datetime import datetime
from ui import format_page, cc


# Wordy Page -----------------------------------------------------
@ui.page('/')
def index():

    format_page()


    def del_letter():
        prev_word = word.value
        word.value = prev_word[:-1]

    def update_word(letter):
        prev_word = word.value
        word.value = prev_word + letter

    def create_b(letter):
        ui.button(letter, on_click=lambda: update_word(letter))

    def clear_guesses():
        app.storage.user["guesses"] = {}
        app.storage.user["guesses_i"] = {}
        update_page()


    def submit_word(typed_word:str):
        typed_word = typed_word.lower()
        points, definition = check_word(typed_word)

        if points > 0:
            guesses = app.storage.user.get("guesses", {})
            guesses[typed_word] = {"def": definition, "points":points}
            app.storage.user["guesses"] = guesses
        else:
            guesses = app.storage.user.get("guesses_i", {})
            guesses[typed_word] = definition
            app.storage.user["guesses_i"] = guesses

        # clear responses
        word.value = ""
        update_page()

    def update_page():
        # update page
        guess_cont.clear()
        with guess_cont:
            with ui.column():
                guess_md, points = guess_parser(app.storage.user.get("guesses", {}))
                ui.markdown("**Guesses**")
                ui.markdown(f"""
                            {guess_md}
                            """)
            with ui.column():
                ui.markdown("**Wrong**")
                guess_md_i = guess_inc(app.storage.user.get("guesses_i", {}))
                ui.markdown(f"""
                            {guess_md_i}
                            """)
            
        stat_container.clear()
        with stat_container:
            max_p = 22
            avg_p = 14
            guess_md = guess_parser(app.storage.user.get("guesses", {}))
            ui.markdown()
            ui.markdown(f"""
                        **Points**: {points}

                        - Average: {avg_p}
                        - Max: {max_p}
                        """)
        
    with ui.row():
        with cc():
            # game card
            vowels, consonants = vows_consonsants()
            word = ui.textarea("Entry")
            with ui.row():
                for v in vowels:
                    create_b(v)
            with ui.row():
                for c in consonants:
                    create_b(c)

            with ui.row():
                ui.button("<-- del", on_click=lambda: del_letter(), color='orange')
                ui.button("Submit", on_click=lambda: submit_word(word.value), color='green')
        with cc():
            stat_container = ui.column()

    with cc():
        guess_cont = ui.element()
    
    update_page()
    ui.button("Clear", on_click=lambda:clear_guesses())

# running the page
ui.run(title="Wordy", port=2999, binding_refresh_interval=0.5, storage_secret="xxx")

# ------------------------------------------------------