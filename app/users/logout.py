from flask import session


def logout():
    '''logout user'''
    if session['loggedin'] is not False:
        session['loggedin'] = False
        session.pop('id')
        session.pop('username')
        session.pop('access-token')
        
        return("you're now logged out"),200
    else:
        return("already logged out"),500