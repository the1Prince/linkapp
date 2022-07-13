from datetime import datetime
from email.policy import default
from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname= db.Column(db.String(64))
    lastname= db.Column(db.String(64))
    username= db.Column(db.String(64),index=True,unique=True)
    email= db.Column(db.String(64),index=True,unique=True)
    password = db.Column(db.Text())
    public_id= db.Column(db.Text())
    
    setup_date=db.Column(db.DateTime(),default=datetime.now(tz=None))

class Contact_group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(64))
    description=db.Column(db.Text())
    user=db.Column(db.String(64))

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname= db.Column(db.String(64))
    lastname= db.Column(db.String(64))
    email= db.Column(db.String(64))
    telephone=db.Column(db.String(20))
    address= db.Column(db.Text())
    group_name=db.Column(db.String(64),default="associate")
    user=db.Column(db.String(64))
