import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from main import models
from main.models import Customer
from main.tests.cutomer import test_add_user

engine = None
Base = models.Base


def init():
    global Base, engine

    engine = db.create_engine('sqlite:///bike_sharing.sqlite')
    # connection = engine.connect()
    # metadata = db.MetaData()
    Base.metadata.create_all(engine)


def get_command(command):
    pass


# in_ = input()
# get_command(in_)
init()
test_add_user(engine)
