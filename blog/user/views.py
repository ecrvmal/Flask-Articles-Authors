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


@user.route('register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))

    errors = []
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
            birth_year=form.birth_year.data,
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
        'users/register.html',
        form=form,
        errors=errors
    )


@user.route('/')
@login_required
def user_list():
    from blog.models import User
    users = User.query.all()
    return render_template(
        'users/list.html',
        users=users,
    )


@user.route('/<int:pk>')
@login_required
def profile(pk: int):
    from blog.models import User

    _user = User.query.filter_by(id=pk).one_or_none()
    if not _user:
        # raise NotFound(f'user id {pk} not found')      # change error message
        return redirect('/users/')                       # or make action  (redirect) on error
    return render_template(
        'users/profile.html',
        user=_user,     # possible to pass any variables. objects
    )