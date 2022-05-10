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
    status = Column(String, default="free")
    loc_x = Column(Integer, default=0)
    loc_y = Column(Integer, default=0)
    total_points = Column(Integer, default=0)

    def __repr__(self):
        return f'User {self.name}'


class Ride(Base):
    __tablename__ = 'ride'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    bike_id = Column(Integer, ForeignKey('bike.id'))
    status = Column(String, default="none")
    distance = Column(Integer, default=0)
    date = Column(Date)
    point = Column(Integer, default=0)

    def __repr__(self):
        return f'Ride {self.id}'


class Bike(Base):
    __tablename__ = 'bike'

    id = Column(Integer, primary_key=True)
    status = Column(String, default="available")
    loc_x = Column(Integer, default=0)
    loc_y = Column(Integer, default=0)

    def __repr__(self):
        return f'Bike {self.id}'
