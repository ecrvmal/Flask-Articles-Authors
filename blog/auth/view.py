from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash


auth = Blueprint('auth', __name__, static_folder='../static')


@auth.route('/login', methods=['POST', 'GET'])   # route registration
def login():

    if request.method == 'GET':         # then return template
        return render_template(
            'auth/login.html'
        )

    username = request.form.get('username')        # get data from form, fill dict
    password = request.form.get('password')        # get data from form, fill dic

    from blog.models import User

    user = User.query.filter_by(username=username).first()
    # print('user',user)
    # print('password',password)
    # print('check passw ', check_password_hash(user.password, password))

    if not user or not check_password_hash(user.password, password):
        flash('Please Check Username and Password')
        return redirect(url_for('.login'))

    login_user(user)
    flash('Logged in successfully.')
    return redirect(url_for('user.user_list'))


@auth.route('/logout')    # route registration
#@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))
