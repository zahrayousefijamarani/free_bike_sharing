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
from main.haversine import haversine
from main.models import Customer, Bike

Base = models.Base

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "se-lab"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(minutes=5)
jwt = JWTManager(app)

engine = db.create_engine('sqlite:///bike_sharing.sqlite')
# connection = engine.connect()
# metadata = db.MetaData()
Base.metadata.create_all(engine)


def make_bikes():
    session = Session(engine)
    bike1 = Bike(status="available", loc_x=1, loc_y=4)
    bike2 = Bike(status="available", loc_x=3, loc_y=10)
    bike3 = Bike(status="available", loc_x=7, loc_y=6)
    session.add(bike1)
    session.add(bike2)
    session.add(bike3)
    session.commit()
    session.close()


if __name__ == "__main__":
    make_bikes()
    app.run()
