# Main Py File...

# Necessary Imports
from CradleControl.IndexCradle import *


# Flask Configuration...
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = "oki_3s3434foa22sdfasdafki"
app.config['SESSION_FILE_THRESHOLD'] = 10
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=0.5)
Session(app)
# login_manager = LoginManager()
# login_manager.login_view = "LoginView"
# login_manager.init_app(app)
# change session length... add logout page


# Home Page. Lead to options
# ----------------------------------------------------------------------------------------------------------------------
@app.route('/')
def frontpage():
    return render_template('ASGMainJumbo.html')


# Blue Print Registry...
# ----------------------------------------------------------------------------------------------------------------------

# CradlePoint Pages
app.register_blueprint(CradleView)
app.register_blueprint(CradleEdit)


# Runs the system
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
