from operator import concat
from tokenize import group
from flask import jsonify, request, session
import pymysql
from app.models import Contact_group,Contact
from app import db

def getGroup(id):
    '''get a single contact group'''
    if session.get("access-token") is not None:
        try:
            group=Contact_group.query.filter_by(id=int(id),user=session['username']).first()
            return jsonify({"id":group.id, "name":group.name, "description":group.description, "user":group.user}),201
        except AttributeError:
            return jsonify({"eroor":"no record found"}),500
    else:
        return jsonify({"error":"invalid session, login to continue"}),500


def getGroups():
    '''get all contact groups'''
    if session.get("access-token") is not None:
        groups=Contact_group.query.filter_by(user=session['username']).all()
        try:
            all_records=[]
            for count in groups:
                all_records.append([count.id,count.name,count.description])
            return jsonify(all_records),201
        except TypeError:
            return jsonify({"error":"no records"}),500
    else:
        return jsonify({"error":"invalid session, login to continue"}),500


def getContact(id):
    '''get a single contact'''
    if session.get("access-token") is not None:
        try:
            contact=Contact.query.filter_by(id=int(id),user=session['username']).first()
            return jsonify({"id":contact.id, "name":contact.firstname, "lastname":contact.lastname, "email":contact.email, "telephone":contact.telephone, "address":contact.address, "group":contact.group_name}),201
             
        except AttributeError:
            return jsonify({"eroor":"no record found"}),500
    else:
        return jsonify({"error":"invalid session, login to continue"}),500




def getContacts(group_name,page):
    '''get all contact'''
    
    if session.get("access-token") is not None:
        try:
            per_page = 20
            contact = Contact.query.filter_by(group_name=group_name,user=session['username']).order_by(Contact.id.desc()).paginate(int(page),per_page,error_out=False)
            all_records=[]
            for count in contact.items:
                all_records.append([count.id,count.firstname,count.lastname,count.email,count.telephone,count.address])
            return jsonify(all_records),201
            
        except AttributeError:
            return jsonify({"eroor":"no record found"}),500
    else:
        return jsonify({"error":"invalid session, login to continue"}),500