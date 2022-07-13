from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app=Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
#app.secret_key=app.config['SERCRET_KEY']
secret=Config.SECRET_KEY

app.register_blueprint(Config.SWAGGER_BLUEPRINT, url_prefix=Config.SWAGGER_URL)


from app import routes,models