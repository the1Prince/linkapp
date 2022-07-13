from operator import concat
from flask import jsonify, request, session
import pymysql
from app.models import Contact_group,Contact
from app import db
import pandas as pd
from werkzeug.utils import secure_filename
import os


ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



def createGroup():
    '''method for inserting new contact group record'''
    data = request.get_json()

    

    if data is not None:
        name=data["name"]
        description=data["description"]
        user=session["username"]
        try:
            group=Contact_group(
                name=name,
                description=description,
                user=user
            )

            db.session.add(group)
            db.session.commit()
            return jsonify({"id":group.id, "name":group.name, "description":group.description}),201
        except pymysql.err.MySQLError as ex:
            return jsonify(str(ex)),500
        except KeyError:
            return jsonify({"error":"invalid session, login to continue"}),500
    else:
        return jsonify({'error':'cannot insert empty data'}),503



def createContact():
    '''method for inserting new contact record'''
    data = request.get_json()

    

    if data is not None:
        firstname= data["firstname"]
        lastname= data["lastname"]
        email= data["email"]
        telephone=data["telephone"]
        address= data["address"]
        group_name=data["group_name"]
        user=session["username"]
        
        try:
            contact=Contact(
                firstname=firstname,
                lastname=lastname,
                email=email,
                telephone=telephone,
                address=address,
                group_name=group_name,
                user=user
            )

            db.session.add(contact)
            db.session.commit()
            return jsonify({"id":contact.id, "firstname":contact.firstname, "lastname":contact.lastname,"email":contact.email,"telephone":telephone,"address":contact.address,"group_name":contact.group_name}),201
        except pymysql.err.MySQLError as ex:
            return jsonify(str(ex)),500
        except KeyError:
            return jsonify({"error":"invalid session, login to continue"}),500
    else:
        return jsonify({'error':'cannot insert empty data'}),503


def bulkUplaod(group_name):
    # get the uploaded file
    
    uploaded_file = request.files['fileName']
    
    if uploaded_file.filename != '':
        
        if session.get("access-token") is not None:
            file_path = "app/uploads/" + session['username'] 
          # set the file path
            if allowed_file(uploaded_file.filename):
                secfile = secure_filename(uploaded_file.filename)
                if not os.path.exists(file_path):
                    os.makedirs(file_path)
                    uploaded_file.save(file_path+secfile)
                else:
                    uploaded_file.save(file_path+secfile)


                # CVS Column Names
                col_names = ['firstname','lastname','email', 'telephone', 'address']
                # Use Pandas to parse the CSV file
                csvData = pd.read_csv(file_path+secfile,names=col_names, header=None)
                # Loop through the Rows
                ar=[]
                for i,row in csvData.iterrows():
                    contact=Contact(
                    firstname=row['firstname'],
                    lastname=row['lastname'],
                    email=row['email'],
                    telephone=row['telephone'],
                    address=row['address'],
                    group_name=group_name,
                    user=session['username']
                )
                ar.append(contact)

                db.session.add_all(ar)
                db.session.flush()
                db.session.commit()
                return jsonify("bulk upload successful")
            else:
                return jsonify({"error":"invalid file, upload csv only"}),500
        else:
            return jsonify({"error":"invalid session, login to continue"}),500
    else:
        return jsonify({'error':'cannot insert empty data'}),503
