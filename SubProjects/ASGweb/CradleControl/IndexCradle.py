# File to expand to the Grey Area
from CradleControl.PyCradleTable import *


# Create Blueprints
temp_link = 'templates'
CradleView = Blueprint('CradleView', __name__, template_folder=temp_link)
CradleEdit = Blueprint('CradleEdit', __name__, template_folder=temp_link)


# Table View to view cradlepoint info, ping and edit
@CradleView.route('/CradleView', methods=["POST", "GET"])
def cradle_view():
    cradles = cradle_view_f(request)
    return render_template('CradleViewTable.html', cradles=cradles)


# Cradle point info edit screen
@CradleEdit.route('/CradleEdit', methods=["POST", "GET"])
def cradle_edit():
    cradle = cradle_edit_f(request)
    if cradle == "updated":
        return redirect(url_for('CradleView.cradle_view'))
    else:
        return render_template('CradleItemTable.html', cradle=cradle)


