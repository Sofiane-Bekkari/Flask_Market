## IMPORT SECTION
from flask import Flask, render_template # MOST IMPORTENT
from flask_sqlalchemy import SQLAlchemy # DATABASE
from flask_bcrypt import Bcrypt # ENCRYPT
from flask_login import LoginManager
## END IMPORT SEC

app = Flask(__name__) # MOST IMPORTENT APP 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' # CONFIGURATION uri FOR FILE market.db
app.config['SECRET_KEY'] = 'df57a2f290b592ec7032b833' # SECRET KEY
db = SQLAlchemy(app) # SETTING UP DATABASE
bcrypt = Bcrypt(app) # HASH PASSWORD
login_manager = LoginManager(app) # LOGIN MANAGEMENT 

from market import route