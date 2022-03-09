from cProfile import label
from flask_wtf import FlaskForm # new package we are install
from wtforms import StringField, PasswordField, SubmitField, Label
from wtforms.validators import Length, EqualTo, Email, DataRequired  # VALIDATOR IMPORTED

# CREATE CLASS REGISTRE FORM
class RegisterForm(FlaskForm): # NEED TO PASS AN ARGUMENT
    username = StringField(label='Enter User Name', validators=[Length(min=3, max=30), DataRequired()])
    email = StringField(label='Email Address', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
    confirm_password = PasswordField(label='Confirm Password', validators=[EqualTo('password'), DataRequired()])# pass it as STRING
    submit = SubmitField(label='Create Account')