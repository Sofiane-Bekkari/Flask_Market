# ROUTES 
from market import app # FROM MARKET PACKAGE
from market.model import Item # FROM SUB MARKET/MODEL
from market.form import RegisterForm # FROM SUB MARKET/FORM
from flask import render_template # NATIVE FLASK

@app.route("/") # FIRST HANDEL PAGE
@app.route("/home") # HOME PAGE
def home_page():
    return render_template('home.html')

@app.route("/market") # MARKET
def market_page():
    # SHOW ITEM TABLE FROM DATABASE
    items = Item.query.all() # ALL ITEMS
    
    return render_template('market.html', items=items)

@app.route("/register") # REGISTER
def register_page():
    form = RegisterForm()

    return render_template('register.html', form=form)







@app.route("/about/<username>")
def about_user(username):
    return f'<h1>Hi, user {username}</h1>'