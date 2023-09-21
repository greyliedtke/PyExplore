"""

"""

# IMPORTS
from nicegui import ui, app
from funcs import dictionary, guess_parser, guess_inc
from wordbank import vows_consonsants
from ui import format_page, cc
from datetime import datetime
import random

class QwState:
    def __init__(self):
        self.day = 20
        self.vowels = ["A", "E", "I"]
        self.consonsants = ["B", "C", "D", "F"]
        self.word_dict = {}
    
    def get_letters(self):
        day = datetime.now().day
        if day != self.day:
            self.day = day
            self.vowels, self.consonsants = vows_consonsants()
            print("new day. clear storage and get new words")
            self.clear()
        return self.vowels, self.consonsants
    
    def clear(self):
        app.storage.clear()
        print("cleared storage")

    def score_word(self, word):
        points = len(word)
        unique_letters = set(word)
        if unique_letters == 6:
            points+=3
        return points

    def check_word(self, word):

        # word already logged
        if word in self.word_dict:
            print("present")
            points = self.score_word(word)
            def_dict = self.word_dict[word]

        else:

            def_dict = dictionary.meaning(word)
            # not a word
            if def_dict is None:
                points = 0
            # new word
            else:
                points = self.score_word(word)
                self.word_dict[word] = def_dict

        return points, def_dict

    
    def get_hint(self):
        # missing words = []
        u_keys = dict(app.storage.user.get("guesses", {}))
        print(set(u_keys.keys()))
        
        print(len(self.word_dict))
        wd_set = set(self.word_dict.keys())
        print(wd_set)

        hint = "none"

        random.shuffle(wd_set)
        for w in wd_set:
            if w not in u_keys:
                hint = self.word_dict[w]
                hint = list(dict(hint).values())
                print(hint)
        # pick random from words
        # provide hint
        synonym = "greyman"
        ui.notify(f"Hint: {hint[0]}")
        
        pass

qw = QwState()

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
        points, definition = qw.check_word(typed_word)

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
            vowels, consonants = qw.get_letters()
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
    ui.button("Hint", on_click=lambda: qw.get_hint())
    ui.button("Clear user", on_click=lambda: clear_guesses())
    ui.button("Clear ALL", on_click=lambda: qw.clear())


# running the page
ui.run(title="Qwordy", port=2999, binding_refresh_interval=0.1, storage_secret="xxx")

# ------------------------------------------------------
