import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import MetaData
from sqlalchemy import create_engine, insert, Column
from sqlalchemy import (Integer, String, DECIMAL)
from sqlalchemy.orm import Session, sessionmaker

# Connection parameters
mysql_args = {
    'host': 'localhost',
    'user': 'root',
    'password': 'server$5401',
    'database': 'splitwise',
    'port': 3306
}

# Create a MySQL database engine
engine = create_engine('mysql+pymysql://{user}:{password}@{host}:{port}/{database}'.format(**mysql_args))
connection = engine.connect()
Base = declarative_base()
# Create all tables defined in the models
# Base.metadata.create_all(engine)
# Create a sessionmaker to interact with the database
Session = sessionmaker(engine)


class Lender(Base):
    __tablename__ = 'lender'
    id = Column(Integer, primary_key=True)
    expense_id = Column(Integer)
    user_id = Column(Integer)
    amount_paid = Column(DECIMAL)


class Borrower(Base):
    __tablename__ = 'borrower'
    id = Column(Integer, primary_key=True)
    expense_id = Column(Integer)
    user_id = Column(Integer)
    amount = Column(DECIMAL)


class Expense(Base):
    __tablename__ = 'expense'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    amount = Column(DECIMAL)
    group_id = Column(Integer)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    phone_number = Column(String(15))
    email = Column(String(50))


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class GroupMember(Base):
    __tablename__ = 'group_member'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    group_id = Column(Integer)