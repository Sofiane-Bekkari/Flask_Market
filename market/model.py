from xml.dom.pulldom import default_bufsize
from market import db ## need to be imported from market dirctory
from market import bcrypt, login_manager ## for password hash / login manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# MODEL FOR USERS
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    hash_password = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owner_user', lazy=True)# RELATIONSHIP TO CONNECT OTHER TABLE

    # STANDER MONEY FORMAT
    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'
        else:
            return f'{self.budget}$'

    # ADDED THIS FOR HASHING PASSWORD
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.hash_password = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    # FOR CHECK THE PASWWORD IN LOGIN PHASE
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.hash_password, attempted_password)


# MODEL DB CLASS ITEM
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    product = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id')) # FOREIGNKEY

    # FOR BETTER VIEW ITEM IN DB
    def __repr__(self):
        return f'Item {self.product}'

    # BUY METHOD
    def buy(self, user):  
        self.owner = user.id
        user.budget -= self.price
        db.session.commit()