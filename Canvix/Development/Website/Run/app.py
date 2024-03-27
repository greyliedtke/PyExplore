"""
main app for qwordy

"""

# imports
from flask import (
    Flask,
    render_template,
    request,
    redirect,
)
from flask import render_template
import socket


# Define Raspberry Pi's IP address and port
HOST = "192.168.0.23"  # Replace with Raspberry Pi's IP address
PORT = 65432  # Port on which the server is listening


def send_socket_cmd(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server
        s.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")
        s.sendall(command.encode("utf-8"))
        print(f"Sent command: {command}")


# flask config
app = Flask(__name__)


# ------------------------------------------------------
@app.route("/about")
def page_about():
    return render_template("about.html")


@app.route("/pi", methods=["POST"])
def page_pi():
    data = request.json  # Get the data sent from the client as JSON
    print(data)
    try:
        print("send socket data")
        send_socket_cmd(data)
    except Exception as e:
        print(e)
    return "hey"

# ------------------------------------------------------
@app.route("/")
def page_home():
    return redirect("/about")
    # return render_template("home.html")

# ------------------------------------------------------
# running app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1234)
