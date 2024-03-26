"""
main app for qwordy

"""

# imports
from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    session,
    make_response,
    redirect,
    url_for,
)

from flask import Blueprint, render_template
from datetime import timedelta
import ast

# flask config
app = Flask(__name__)

# ------------------------------------------------------
@app.route("/about")
def page_about():
    return render_template(
            "about.html"
        )

# ------------------------------------------------------
@app.route("/")
def page_home():
    return redirect("/about")
    # return render_template("home.html")


# ------------------------------------------------------
# running app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1234)