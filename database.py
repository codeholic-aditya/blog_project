from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
# from dependencies import DATABASE_URL

Base = declarative_base()       # Base class for Models

engine = create_engine("sqlite:///./blog_project.db")    # create engine

SessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)   #create sessionmaker

def get_db():
    """ 
    This function use to make session and use for connection to database
    """
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
