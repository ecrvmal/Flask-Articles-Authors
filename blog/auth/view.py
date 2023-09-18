from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from psycopg2 import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash

from blog.extensions import db
from blog.forms.user import UserLoginForm, UserRegisterForm


auth = Blueprint('auth', __name__, static_folder='../static')


@auth.route('/login', methods=['POST', 'GET'])   # route registration
def login():
    """
    The login function handles the logic for a user logging in.
        If the request method is GET, then we return our login template.
        If it's POST, then we validate our form and log them in if everything checks out.

    :return: A template
    :doc-author: Trelent
    """
    if request.method == 'GET':         # then return template
        if current_user.is_authenticated:
            return redirect(url_for('user.profile', pk=current_user.id))

    errors = []
    form = UserLoginForm(request.form)  # request.form - If there is a value for key,
    # the form  will display the value after page reload
    # this need for debugging
    if request.method == 'POST' and form.validate_on_submit():

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
    return render_template(
        'auth/login.html',
        form=form,
        errors=errors
    )


@auth.route('/logout')    # route registration
@login_required
def logout():
    """
    The logout function logs the user out of their account.
        It does this by calling the logout_user() function from Flask-Login, which removes all session data and cookies.

    :return: A redirect to the login page
    :doc-author: Trelent
    """
    logout_user()
    return redirect(url_for('.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    The register function is responsible for handling the registration of new users.
    It will render a form to the user, and then validate that form when it is submitted.
    If validation passes, it will create a new User object and add it to the database.

    :return: A redirect to the user profile
    :doc-author: Trelent
    """
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))

    errors = []
    from blog.models import User
    form = UserRegisterForm(request.form)   # request.form - If there is a value for key,
                                            # the form  will display the value after page reload
                                            # this need for debugging
    if request.method == 'POST' and form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():             # User is model
            form.email.errors.append("email isn't uniq")
            return render_template('users/register.html', form=form)
        if User.query.filter_by(username=form.username.data).count():             # User is model
            form.username.errors.append("username isn't uniq")
            return render_template('users/register.html', form=form)

        _user = User(
            username=form.username.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data),
        )

        db.session.add(_user)
        try:
            db.session.commit()
        except IntegrityError:
            errors.append("Database Commit Error")
        else:
            login_user(_user)

    return render_template(
        'auth/register.html',
        form=form,
        errors=errors
    )

