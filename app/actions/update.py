from operator import concat
from tokenize import group
from flask import jsonify, request, session
import pymysql
from app.models import Contact_group,Contact
from app import db

def update_group(id):
    data=request.get_json()


    if data is not None:
        
        name=data["name"]
        description=data["description"]
        user=session["username"]
        try:
            group=Contact_group.query.filter_by(id=int(id),user=user).first()
            
            if group is not None:
                group.name=name,
                group.description=description,
                group.user=user
            else:
                return jsonify({"error":"no records found"}),500
            

            
            db.session.commit()
            return jsonify({"id":group.id, "name":group.name, "description":group.description}),201
        except pymysql.err.MySQLError as ex:
            return jsonify(str(ex)),500
        except KeyError:
            return jsonify({"error":"invalid session, login to continue"}),500
    else:
        return jsonify({'error':'cannot insert empty data'}),503


def updateContact(id):
    data=request.get_json()


    if data is not None:
        
        firstname= data["firstname"]
        lastname= data["lastname"]
        email= data["email"]
        telephone=data["telephone"]
        address= data["address"]
        group_name=data["group_name"]
        user=session["username"]
        try:
            contact=Contact.query.filter_by(id=int(id),user=user).first()
            
            if contact is not None:
                firstname=firstname,
                lastname=lastname,
                email=email,
                telephone=telephone,
                address=address,
                group_name=group_name,
                user=user
            else:
                return jsonify({"error":"no records found"}),500
            

            
            db.session.commit()
            return jsonify({"id":contact.id, "name":contact.firstname, "lastname":contact.lastname, "email":contact.email, "telephone":contact.telephone, "address":contact.address, "group":contact.group_name}),201
        except pymysql.err.MySQLError as ex:
            return jsonify(str(ex)),500
        except KeyError:
            return jsonify({"error":"invalid session, login to continue"}),500
    else:
        return jsonify({'error':'cannot insert empty data'}),503