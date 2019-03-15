from flask_wtf import FlaskForm
from wtforms import Form, StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed

class ProfileForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('m','Male'),('f','Female')], validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    location = StringField('Located at', validators=[DataRequired()])
    biography = TextAreaField('Biography', validators=[DataRequired()])
    picture = FileField('Profile Photo', 
    validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
        ])
    submit = SubmitField('Send')