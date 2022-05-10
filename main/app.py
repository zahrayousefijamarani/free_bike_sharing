import datetime

from flask import Flask
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import sqlalchemy as db
from sqlalchemy.orm import Session

from main import models
from main.models import Customer

Base = models.Base

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "se-lab"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(minutes=5)
jwt = JWTManager(app)

engine = db.create_engine('sqlite:///bike_sharing.sqlite')
# connection = engine.connect()
# metadata = db.MetaData()
Base.metadata.create_all(engine)





if __name__ == "__main__":
    app.run()
