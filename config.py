from flask_swagger_ui import get_swaggerui_blueprint


class Config(object):
    SQLALCHEMY_DATABASE_URI= 'sqlite:///contacts.db'     #'mysql+pymysql://root:root@mysqldbase:3306/contacts'
    #MONGO_DNAME='linkapp'
    #MONGO_URI='mongodb://linkapp_db_1:27017/linkapp?compressors=disabled&gssapiServiceName=mongodb' 
    #MONGODB_SETTINGS = {
    #'db': 'linkapp',
    #'host': 'linkapp_db_1',
    #'port': 27017,
    
    #}
    
    SECRET_KEY = '8de9ceda-f1c9-4b62-8e1b-36fe45f98ecc'


    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    SWAGGER_BLUEPRINT = get_swaggerui_blueprint(SWAGGER_URL,API_URL,
    config = {
        'app_name':'LinkApp API'
    }
    )
