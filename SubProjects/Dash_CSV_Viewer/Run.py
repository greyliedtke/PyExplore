""" 
Script to host the app and handle plotting web pages
"""

# Dash index to handle different pages
from dash.dependencies import Input, Output
from DashHandling.DashApp import app


# runs the server
if __name__ == '__main__':
    app.run_server(debug=True)

# end of script
