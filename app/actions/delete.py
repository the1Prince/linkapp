from operator import concat
from tokenize import group
from flask import jsonify, request, session
import pymysql
from app.models import Contact_group,Contact
from app import db

def delete_group(id):
        
        
    user=session["username"]
    try:
        group=Contact_group.query.filter_by(id=int(id),user=user).first()
            
        if group is not None:
            db.session.delete(group)
            db.session.commit()
            return jsonify("delete successful"),201
        else:
            return jsonify({"error":"no records found"}),500
       
    except pymysql.err.MySQLError as ex:
        return jsonify(str(ex)),500
    except KeyError:
        return jsonify({"error":"invalid session, login to continue"}),500
  


def deleteContact(id):
        
        
    user=session["username"]
    try:
        contact=Contact.query.filter_by(id=int(id),user=user).first()
            
        if contact is not None:
            db.session.delete(contact)
            db.session.commit()
            return jsonify("delete successful"),201
        else:
            return jsonify({"error":"no records found"}),500
       
    except pymysql.err.MySQLError as ex:
        return jsonify(str(ex)),500
    except KeyError:
        return jsonify({"error":"invalid session, login to continue"}),500
  