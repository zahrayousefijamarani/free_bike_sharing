import sqlite3 as lite
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

    def __repr__(self):
        return f'User {self.name}'


engine = db.create_engine('sqlite:///bike_sharing.sqlite')
connection = engine.connect()
metadata = db.MetaData()

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

user = User(name='Amir Abbas', password='thispass')
session.add(user)
session.commit()

print(user.id)

query = session.query(User).filter(User.name.like('%Amir%'))


print(query.all())

# census = db.Table('census', metadata, autoload=False)


# print(census.columns)