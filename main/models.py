from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    status = Column(String)
    loc_x = Column(Integer)
    loc_y = Column(Integer)
    total_points = Column(Integer)

    def __repr__(self):
        return f'User {self.name}'


class Ride(Base):
    __tablename__ = 'ride'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    bike_id = Column(Integer, ForeignKey('bike.id'))
    status = Column(String)
    distance = Column(Integer)
    date = Column(Date)
    point = Column(Integer)

    def __repr__(self):
        return f'Ride {self.id}'


class Bike(Base):
    __tablename__ = 'bike'

    id = Column(Integer, primary_key=True)
    status = Column(String)
    loc_x = Column(Integer)
    loc_y = Column(Integer)

    def __repr__(self):
        return f'Bike {self.id}'
