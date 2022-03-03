## IMPORT SECTION

from flask import Flask, render_template # MOST IMPORTENT

## END IMPORT SEC

app = Flask(__name__) # MOST IMPORTENT APP 

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/market")
def market_page():
    items = {"id":1, "name":'phone', "price":50}
    return render_template('market.html', items=items)






@app.route("/about/<username>")
def about_user(username):
    return f'<h1>Hi, user {username}</h1>'


