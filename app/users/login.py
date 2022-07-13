import jwt
from app import secret
from app.models import Users
from datetime import datetime, timedelta
from flask import request, jsonify, session
from werkzeug.security import check_password_hash
from pymysql.err import OperationalError



import app


def login():
    '''Login user'''
    
    data = request.get_json()

    if data and data is not None:
        username = data['username']
        password = data['password']
        
        #get user details
        try:
            current_user = Users.query.filter_by(username=username).first()
            u=current_user.username
            passw=current_user.password

            if check_password_hash(passw,password):
            #session
                session['loggedin'] = True
                session['id'] = current_user.id
                session['username'] = current_user.username
            
            # generates the JWT Token
                token = jwt.encode({
                    'public_id': current_user.public_id,
                    'exp' : datetime.utcnow() + timedelta(minutes = 30)
                }, secret)
            
                session['access-token']=token
                return jsonify({'token' : session['access-token']}), 201
            else:
                return jsonify('wrong username or password'),400
        except OperationalError as ex :
            return jsonify(str(ex)),500



    
    else:
        return jsonify('provide login credentials'),500