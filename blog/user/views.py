from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user, login_user
from sqlalchemy.exc import IntegrityError

from blog.models import User
from blog.extensions import db
from werkzeug.exceptions import NotFound
from werkzeug.security import generate_password_hash
from blog.forms.user import UserRegisterForm


user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')
# the Blueprint will be registered in app.py
# when request  localhost/users   > goes to the Bluepront (url_prefix param)
# when request  localhost/users   > goes to function under @user.route('/')

# USERS = {1: 'Alice', 2: 'John', 3: 'Mike'}


@user.route('/')
# @login_required
def user_list():
    """
    The user_list function is responsible for rendering the user list page.
    It queries the database for all users and passes them to a template.

    :return: A rendered template
    :doc-author: Trelent
    """
    from blog.models import User
    users = User.query.all()
    return render_template(
        'users/list.html',
        users=users,
    )


@user.route('/<int:pk>')
@login_required
def profile(pk: int):
    """
    The profile function , when visited, will display the profile of a user.
        Args:
            pk (int): The primary key of the user to get.

    :param pk: int: Specify the user id
    :return: A redirect to the users page
    :doc-author: Trelent
    """
    from blog.models import User

    _user = User.query.filter_by(id=pk).one_or_none()
    if not _user:
        # raise NotFound(f'user id {pk} not found')      # change error message
        return redirect('/users/')                       # or make action  (redirect) on error
    return render_template(
        'users/profile.html',
        user=_user,     # possible to pass any variables. objects
    )