from cProfile import label
from flask_wtf import FlaskForm # new package we are install
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError  # VALIDATOR IMPORTED
from market.model import User # User to check username & email is alraedy exist

# CREATE CLASS REGISTRE FORM
class RegisterForm(FlaskForm): # NEED TO PASS AN ARGUMENT FlaskForm

    ## VALIDATION USERNAME
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! PLease try a different username')
    
     ## VALIDATION EMAIL
    def validate_email(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('Email address already exists! PLease try a different email address')


    username = StringField(label='Enter User Name', validators=[Length(min=3, max=30), DataRequired()])
    email = StringField(label='Email Address', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
    confirm_password = PasswordField(label='Confirm Password', validators=[EqualTo('password'), DataRequired()])# pass it as STRING
    submit = SubmitField(label='Create Account')


 # LOGIN FORM
class LoginForm(FlaskForm):
    username = StringField(label='Enter Name',  validators=[DataRequired()])
    password = PasswordField(label='Password',  validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

# BUY FORM
class BuyForm(FlaskForm):
    submit = SubmitField(label='Buy Item')

# SELL FORM
class SellForm(FlaskForm):
    submit = SubmitField(label='Sell Item')
