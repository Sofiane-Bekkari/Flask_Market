# ROUTES 
from market import app, db # FROM MARKET PACKAGE
from market.model import Item, User # FROM SUB MARKET/MODEL
from market.form import RegisterForm, LoginForm # FROM SUB MARKET/FORM
from flask import render_template, redirect, url_for, flash # NATIVE FLASK
from flask_login import login_user, logout_user, login_required # LOGIN SYSTEM


@app.route("/") # FIRST HANDEL PAGE
@app.route("/home") # HOME PAGE
def home_page():
    return render_template('home.html')

@app.route("/market") # MARKET
@login_required # for require user to log before visted the page!
def market_page():
    # SHOW ITEM TABLE FROM DATABASE
    items = Item.query.all() # ALL ITEMS
    
    return render_template('market.html', items=items)

@app.route("/register", methods=['GET','POST']) # REGISTER
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User( username=form.username.data, email=form.email.data,
        password=form.password.data )

        db.session.add(user_to_create)
        db.session.commit()

        login_user(user_to_create) # SUCCESSFULY LOGIN
        flash(f'Successful! Created an account you are logged in as: {user_to_create.username}', category='success') # WELCOME MSG!

        return redirect(url_for('market_page'))

    # CATCH ERRORS
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'HERE ERR-MSG: {err_msg}', category='danger')
    #print(f'Username:  {form.username.data} Email: {form.email.data} Password: {form.password.data} Con-Password: {form.confirm_password.data}')
    print("BACK!!!")
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET','POST']) # LOGIN
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password.data
            ):
            login_user(attempted_user) # SUCCESSFULY LOGIN
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success') # WELCOME MSG!
            return redirect(url_for('market_page')) # DEDIRECT TO THIS PAGE
        else:
            flash(f'Username or Password was uncorrect! Please try again.', category='danger') # FIALD MSG! 

    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():

    logout_user()
    flash("You have been logged out!", category='info')

    return redirect(url_for("home_page"))


### THESE FOR TESTING PURPOSES
@app.route('/admin')
@login_required # MANDATORY 
def admin_page():
    return f'<h1>Admin page is welcoming!</h1> I believe you do whatever you want here so..'

@app.route("/about/<username>")
def about_user(username):
    return f'<h1>Hi, user {username}</h1>'