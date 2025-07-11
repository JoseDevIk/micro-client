from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .configuration import Config

#Prepare connection
engine = create_engine(Config.SQL_ALCHEMY_DATABASE_URI)

#Create ORM session
orm_session = sessionmaker(bind=engine)