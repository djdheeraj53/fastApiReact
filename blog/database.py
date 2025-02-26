from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHAMY_DATAASE_URL = 'sqlite:///./blog.db'

engine = create_engine(SQLALCHAMY_DATAASE_URL, connect_args={"check_same_thread": False}) # create engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()