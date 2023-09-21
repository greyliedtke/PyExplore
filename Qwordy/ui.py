from nicegui import ui, app
from contextlib import contextmanager

def format_page():
    # HEADER
    with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between'):
        with ui.row():
            # time_display()
            ui.label('Qwordy')

        ui.button(on_click=lambda: right_drawer.toggle(), icon='menu').props('flat color=white')

    # RIGHT SIDE
    with ui.right_drawer(fixed=False).style('background-color: #ebf1fa').props('bordered') as right_drawer:
        ui.link("Feedback Form", "https://www.google.com/")

        ui.markdown(
            """
        ### TODO
        - Improvements
            - faster button respons
        - Stats
            - average person score
            - max score
        - Points
            - based on how rare?
            """
        )

@contextmanager
def cc():
    '''Custom page frame to share the same styling and behavior across all pages'''
    with ui.card().classes('bg-[#e6e6e6] col-6 self-stretch rounded') \
            .style('box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1)'):
        yield

