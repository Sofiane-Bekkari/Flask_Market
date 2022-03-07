from cProfile import label
from flask_wtf import FlaskForm # new package we are install
from wtforms import StringField, PasswordField, SubmitField, Label

# CREATE CLASS REGISTRE FORM
class RegisterForm(FlaskForm): # NEED TO PASS AN ARGUMENT
    username = StringField(label='Enter User Name')
    email = StringField(label='Email Address')
    password = PasswordField(label='Password')
    confirm_password = PasswordField(label='Confirm Password')
    submit = SubmitField(label='Create Account')