"""

"""

# IMPORTS
from nicegui import ui, app
from funcs import check_word, guess_parser, guess_inc
from wordbank import vows_consonsants
from ui import format_page, cc
from datetime import datetime


class LexiState:
    def __init__(self):
        self.day = 0
        self.vowels = "A, E, I"
        self.consonsants = "B, C, D, E"
    
    def check_day(self):
        day = datetime.now().day
        if day != self.day:
            self.day = day
            print("new day. clear storage and get new words")
            self.clear()

    def get_letters(self):
        self.check_day()
        return self.vowels, self.consonsants
    
    def clear(self):
        app.storage.clear()
        print("cleared storage")

lexis = LexiState()

# Wordy Page -----------------------------------------------------
@ui.page("/")
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

    def submit_word(typed_word: str):
        typed_word = typed_word.lower()
        points, definition = check_word(typed_word)

        if points > 0:
            guesses = app.storage.user.get("guesses", {})
            guesses[typed_word] = {"def": definition, "points": points}
            app.storage.user["guesses"] = guesses
        else:
            guesses = app.storage.user.get("guesses_i", {})
            guesses[typed_word] = definition
            app.storage.user["guesses_i"] = guesses

        uid = app.storage.browser['id']
        tn = datetime.now()
        tn = tn.strftime("%Y-%m-%d %H:%M:%S")
        print(f"LOG:{uid}, {points}, {typed_word}, {tn}")

        # clear responses
        word.value = ""
        update_page()

    def update_page():
        # update page
        guess_cont.clear()
        with guess_cont:
            with ui.expansion("Definitions", icon="done"):
                guess_md, points = guess_parser(app.storage.user.get("guesses", {}))
                with ui.scroll_area():
                    ui.markdown(
                        f"""
                                {guess_md}
                                """
                    )
            with ui.expansion("incorrect", icon="thumb_down").classes("w-full"):
                guess_md_i = guess_inc(app.storage.user.get("guesses_i", {}))
                ui.markdown(
                    f"""
                            {guess_md_i}
                            """
                )
            with ui.expansion("Leaderboard", icon="emoji_events"):
                ui.markdown(
                    f"""
                            - Average: {17}
                            - Max: {20}
                    """
                    )

        p_button.set_text(points)

    with ui.row():
        with cc():
            # game card
            vowels, consonants = lexis.get_letters()
            word = ui.input("Word")
            with ui.row():
                for v in vowels:
                    create_b(v)
            with ui.row():
                for c in consonants:
                    create_b(c)

            with ui.row():
                ui.button("<-- del", on_click=lambda: del_letter(), color="orange")
                ui.button(
                    "Submit", on_click=lambda: submit_word(word.value), color="green"
                )
        with cc():
            with ui.dialog() as points_diag, ui.card():
                ui.markdown(
                    """
                ### Instructions
                - create as many words as you can from
                - 3 vowels
                - 4 consonants
                
                ### Points
                - 1 letter = 1 points
                - use all letters = 3 points
                            """
                )

                ui.button("Close", on_click=points_diag.close)

            with ui.button("Points", on_click=lambda: points_diag):
                p_button = ui.badge(0, color="green").props("floating")

            guess_cont = ui.element()

    update_page()
    ui.button("Clear user", on_click=lambda: clear_guesses())
    ui.button("Clear ALL", on_click=lambda: lexis.clear())


# running the page
ui.run(title="Lexography", port=2999, binding_refresh_interval=0.1, storage_secret="xxx")

# ------------------------------------------------------
