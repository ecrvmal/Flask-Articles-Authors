from flask import Blueprint, render_template, redirect
from flask_login import login_required

report = Blueprint('report', __name__, url_prefix='/reports', static_folder='../static')
# the Blueprint will be registered in app.py
# when request  localhost/users   > goes to the Bluepront (url_prefix param)
# when request  localhost/users   > goes to function under @user.route('/')


@report.route('/')
@login_required
def report_list():

    # return 'Hello_report'
    """
    The report_list function is a route that returns the list.html template
        with a list of reports passed in as an argument.

    :return: A string, which is the name of the template to render
    """
    return render_template('reports/list.html', reports=[1, 2, 3, 4, 5])