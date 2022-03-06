# ROUTES 
from market import app
from market.model import Item
from flask import render_template

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/market")
def market_page():
    # SHOW ITEM TABLE FROM DATABASE
    items = Item.query.all() # ALL ITEMS
    
    return render_template('market.html', items=items)






@app.route("/about/<username>")
def about_user(username):
    return f'<h1>Hi, user {username}</h1>'