import wtforms
from wtforms import StringField, validators, PasswordField, SubmitField, IntegerField, TextAreaField
from flask_wtf import FlaskForm


class CreateArticleForm(FlaskForm):
    title = StringField('Title', [validators.DataRequired(),])
    text = TextAreaField('Text',)
    submit = SubmitField('Create')
