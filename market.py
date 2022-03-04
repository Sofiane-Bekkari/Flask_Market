## IMPORT SECTION

from flask import Flask, render_template # MOST IMPORTENT
from flask_sqlalchemy import SQLAlchemy # DATABASE

## END IMPORT SEC

app = Flask(__name__) # MOST IMPORTENT APP 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' # CONFIGURATION uri FOR FILE market.db
db = SQLAlchemy(app) # SETTING UP DATABASE


# MODEL DB CLASS
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    product = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    # FOR BETTER VIEW ITEM IN DB
    def __repr__(self):
        return f'Item {self.product}'

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


