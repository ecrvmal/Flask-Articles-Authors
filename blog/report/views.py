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
    return render_template('reports/list.html', reports=[1, 2, 3, 4, 5])