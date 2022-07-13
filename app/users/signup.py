import json

import pymysql

from app.models import Users
import uuid
from app import db
from werkzeug.security import generate_password_hash
from flask import request, jsonify
from datetime import datetime

from re import compile

PASSWORD_REGEX = compile(r'\A(?=\S*?\d)(?=\S*?[A-Z])(?=\S*?[a-z])\S{6,}\Z')


def password_is_valid(password):
    return PASSWORD_REGEX.match(password) is not None

def signUp():
    '''create a new user or signup'''
    data = request.get_json()

    if data and data is not None:
        fname=data['firstname']
        lname=data['lastname']
        uname=data['username']
        em=data['email']
        pw=data['password']
        cm=data['confirm']
        pd=str(uuid.uuid4())
        

        
        try:
            
            
            
            if pw is not None and em is not None and uname is not None:
                if password_is_valid(pw):
                    if pw == cm:
                        password= generate_password_hash(cm)

                        user = Users(
                            firstname=fname,
                            lastname=lname,
                            username=uname,
                            email=em,
                            password=password,
                            public_id=pd,
                            
                            setup_date=datetime.now(tz=None)
                        )
                        

                        db.session.add(user)
                        db.session.commit()

                        return json.dumps({
                            'id':user.id, 'firstname':user.firstname, 'lastname':user.lastname, \
                            'username':user.username,'email':user.email,'public_id':user.public_id,\
                                'setup_date':user.setup_date
                        },sort_keys=True, indent=4, default=str)
                    else:
                        return jsonify('password and confirm password does not match'),500
                else:
                    return jsonify('Weak password, Password must be at least 8 characters long, must contain Characters, Numbers, Upper and Lower case letters'),500
            else:
                return jsonify('password fields are mandatory, provide password and confirm'),500
            
        except pymysql.err.MySQLError as ex:
            return jsonify(str(ex)),400
        
       
    

    else:
        return jsonify({'error':'empty data, provide data for the specified fields to create a new user'}),500