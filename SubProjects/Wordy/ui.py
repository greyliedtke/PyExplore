from nicegui import ui, app
from contextlib import contextmanager

def format_page():
    # HEADER
    with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between'):
        with ui.row():
            # time_display()
            ui.label('Wordy')

        ui.button(on_click=lambda: right_drawer.toggle(), icon='menu').props('flat color=white')

    # RIGHT SIDE
    with ui.right_drawer(fixed=False).style('background-color: #ebf1fa').props('bordered') as right_drawer:
        ui.link("Google", "https://www.google.com/")

        ui.markdown(
            """
        ### Instructions
        - Points:
            - 1 letter = 1 points
            - use all letters = 3 points
        - After 3 submissions, see the best submissions of day
        - See stats of how you did compared to others

        ### TODO
        - POINTS
        - Stats
            - avg total points
            - largest points
            

            """
        )

@contextmanager
def cc():
    '''Custom page frame to share the same styling and behavior across all pages'''
    with ui.card().classes('bg-[#e6e6e6] col-6 self-stretch rounded') \
            .style('box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1)'):
        yield

