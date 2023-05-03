""" Layout file to set layouts of all dash interfaces """
# dash / plotly imports
from dash import dash_table, dcc, html
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# front page  ----------------------------------------------------------------------------------------------------------
main_layout = html.Div([
    # select csv file
    dcc.Upload(
            id='csv_file_select',
            children=html.Div([
                'Select a CSV File '
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
            },
            multiple=True,
        ),
    html.Div(id='csv_analysis'),

])


# ----------------------------------------------------------------------------------------------------------------------
# main csv viewing interface
csv_fig = make_subplots(specs=[[{"secondary_y": True}]])
csv_fig.update_layout(height=800)
csv_fig.update_xaxes(rangemode="nonnegative")   # make the figure have better axis options


# view after a csv has been selected
def csv_view(df):
    csv_viewer = html.Div([

        # create table
        dash_table.DataTable(
            id='csv_view_table',
            columns=(
                    [{'id': p, 'name': p, "hideable": True} for p in df]
            ),
            data=df.to_dict("records"),
            # editable=True,
            sort_action='native',
            filter_action='native',
            page_size=10,
            export_format='csv'
        ),
        html.Br(),

        # Provide column names as option for x axis
        dcc.Dropdown(
            id='csv_view_fig_x',
            options=[{'label': i, 'value': i} for i in df],
        ),
        html.Br(),
        dcc.Dropdown(
            id='csv_view_fig_y1',
            options=[{'label': i, 'value': i} for i in df],
            multi=True,
        ),
        html.Br(),
        dcc.Dropdown(
            id='csv_view_fig_y2',
            options=[{'label': i, 'value': i} for i in df],
            multi=True,
        ),


        # html.Div(id='csv_view-output-container'),
        # html.Label(id='csv_view_x_selected', children="csv_view_child"),
        # standard plot of everything vs first column of table
        dcc.Graph(
            id='csv_view_fig',
            figure=csv_fig,
            config={'scrollZoom': True},
        ),
    ])
    return csv_viewer

# end of layout pages
