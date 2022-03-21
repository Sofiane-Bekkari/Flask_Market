from xml.dom.pulldom import default_bufsize
from market import db ## need to be imported from market dirctory
from market import bcrypt ## for password hash

# MODEL FOR USERS
class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    hash_password = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owner_user', lazy=True)# RELATIONSHIP TO CONNECT OTHER TABLE

    # ADDED THIS FOR HASHING PASSWORD
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.hash_password = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

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