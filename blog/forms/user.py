from wtforms import StringField, validators, PasswordField, SubmitField, IntegerField
from flask_wtf import FlaskForm


class UserRegisterForm(FlaskForm):
    username = StringField('Username')
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('E-mail', [validators.DataRequired(),
                                   # validators.Length(),
                                   validators.Email(),
                                   ])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm_password', message='Field must be equal to password'),
    ])
    confirm_password = PasswordField('Confirm Password', [validators.DataRequired()])
    birth_year = IntegerField('Birth Year')

    submit = SubmitField('Register')


class UserLoginForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Login')

