# from sqlalchemy.ext.declarative import declarative_base
# import sqlalchemy as db
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, ForeignKey, Date
# from sqlalchemy.orm import sessionmaker
#
# event_base = declarative_base()
#
#
# class FinishRideEvent(event_base):
#     __tablename__ = 'finishrideevent'
#
#     id = Column(Integer, primary_key=True)
#     status = Column(String, default="pending")
#     ride_id = Column(Integer)
#
#     def __repr__(self):
#         return f'Ride Id {self.ride_id}'

class User:
    def __init__(self, customer):
        self.id = customer.id
        self.username = customer.username
        self.password = customer.password
        self.status = customer.status
        self.loc_x = customer.loc_x
        self.loc_y = customer.loc_y
        self.total_points = customer.total_points


class Riding:
    def __init__(self, ride):
        self.id = ride.id
        self.customer_id = ride.customer_id
        self.bike_id = ride.bike_id
        self.status = ride.status
        self.distance = ride.distance
        self.date = ride.date
        self.point = ride.point
