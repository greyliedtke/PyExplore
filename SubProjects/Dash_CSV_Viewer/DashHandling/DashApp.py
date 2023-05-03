"""
File to house dash app
"""
from dash.dependencies import Input, Output, State
import pandas as pd
from DashHandling.DashLayouts import main_layout, csv_view, csv_fig
import dash
from dash import dcc, html
import base64, io

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
            df['index'] = df.index
            # print('good df!')
            return csv_view(df)


    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])


@app.callback(
    Output('csv_analysis', 'children'),
    Input('csv_file_select', 'contents'),
    State('csv_file_select', 'filename')
    )
def csv_callback(list_of_contents, list_of_names):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n) for c, n in
            zip(list_of_contents, list_of_names)]
        return children

# callback for updating figure of 2 y axis plot ---------------------------------------------------------------------
@app.callback(
    # Output(component_id='fig_x_selected', component_property='children'),
    Output(component_id='csv_view_fig', component_property='figure'),
    Input(component_id='csv_view_table', component_property='data'),
    Input(component_id='csv_view_fig_x', component_property='value'),
    Input(component_id='csv_view_fig_y1', component_property='value'),
    Input(component_id='csv_view_fig_y2', component_property='value'),
)
def update_csv_fig(df, x_axis, y1_axis, y2_axis):
    df = pd.DataFrame.from_dict(df)
    if x_axis is not None:
        # clear previous figure data
        csv_fig.data = []

        # selected x array to plot
        x_array = df[x_axis].to_numpy()

        # loop through other columns
        if y1_axis is not None:
            for col in y1_axis:
                y_array = df[col].to_numpy()
                csv_fig.add_scatter(
                    x=x_array,
                    y=y_array,
                    name=f"{col}",
                    yaxis=f"y1",
                    secondary_y=False,
                    # side="left"
                )
        if y2_axis is not None:
            for col in y2_axis:
                y_array = df[col].to_numpy()
                csv_fig.add_scatter(
                    x=x_array,
                    y=y_array,
                    name=f"{col}",
                    yaxis=f"y2",
                    secondary_y=True,
                    # side="right"
                )
    return csv_fig

# function to figure out path name... this has trouble at greater than 1 directory...
def path_filter(path):
    if path[0] == "/":
        path = path[1:]
    path_build = []
    split_path = path.split("/")
    for p in split_path:
        if p not in path_build:
            path_build.append(p)
    seperator = "/"
    path = seperator.join(path_build)
    return path

# Present html page from url path
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    # Main Page
    if pathname == "/":
        return main_layout

    # Standard view for viewing a csv file
    elif ".csv" in pathname:
        pathname = path_filter(pathname)
        return csv_view(pathname)

    else:
        return '404'
