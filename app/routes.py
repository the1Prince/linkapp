
from functools import wraps

import jwt
from app import app,db,secret
from app.users import signup,login,logout
from app.models import  Users
from flask import jsonify, redirect, request, session
from app.actions import post, get, update,delete
from config import Config



  
# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        
        # jwt is passed in the request header
        if session['access-token'] is not None:
            token = session['access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
  
        try:
            # decoding the payload to fetch the stored details
            user=Users()
            data = jwt.decode(token, secret, algorithms=['HS256'])
            current_user = user.query.filter_by(public_id=data['public_id']).first()
            
        except jwt.exceptions.ExpiredSignatureError as ex:
            return jsonify({
                'message' : ex
            }), 401
        # returns the current logged in users contex to the routes
        return  f(*args, **kwargs)
  
    return decorated
  



@app.route('/')
@app.route('/imdex', methods=['GET','POST'])
def index():
    return redirect(Config.SWAGGER_URL)

#######################################################
#############user routes#####
@app.route('/v2.0/signup/', methods=['POST'])
def user_signup():
    register=signup.signUp()
    return (register)


@app.route('/v2.0/login/', methods=['POST'])
def user_login():
    login_user=login.login()
    return(login_user)


@app.route('/v2.0/logout/',methods=['POST'])
@token_required
def user_logout():
    logout_user=logout.logout()
    return(logout_user)



#############################################################
#################contact group actions##########
@app.route('/v2.0/group', methods=['POST'])
def post_group():
    group=post.createGroup()
    return(group)

@app.route('/v2.0/group/<id>', methods=['GET'])
def get_group(id):
    group=get.getGroup(id)
    return(group)

@app.route('/v2.0/group', methods=['GET'])
def get_groups():
    groups=get.getGroups()
    return(groups)

@app.route('/v2.0/group/<id>',methods=["PUT"])
def update_group(id):
    group=update.update_group(id)
    return(group)

@app.route('/v2.0/group/<id>', methods=['DELETE'])
def delete_group(id):
    deleteGroup=delete.delete_group(id)
    return(deleteGroup)

############################################################
#################end of contact group actions#####

#################################################################
################contact####################
@app.route('/v2.0/contact',methods=['POST'])
def create_contact():
    contact=post.createContact()
    return(contact)

@app.route('/v2.0/contact/<group_name>', methods=['POST'])
def bulk_upload(group_name):
    contact=post.bulkUplaod(group_name)
    return(contact)


@app.route('/v2.0/contact/<id>',methods=['GET'])
def get_contact(id):
    contact=get.getContact(id)
    return(contact)

@app.route('/v2.0/contact/<group_name>/<page>',methods=['GET'])
def get_contacts(group_name,page):
    contacts=get.getContacts(group_name,page)
    return(contacts)

@app.route('/v2.0/contact/<id>',methods=['PUT'])
def update_contact(id):
    contact=update.updateContact(id)
    return(contact)

@app.route('/v2.0/contact/<id>',methods=['DELETE'])
def delete_contact(id):
    contact=delete.deleteContact(id)
    return(contact)

############################################################
#################end of contact actions#####