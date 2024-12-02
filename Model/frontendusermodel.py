from sqlalchemy import Column,Integer,String,ForeignKey
from database import Base


class FrontUserModel(Base):
    __tablename__="frontend_user"   # frontendusers
    id= Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String, index=True, unique=True) #unique
    firstname = Column(String, index=True,nullable=True) #null
    lastname = Column(String, index=True, nullable=True) #null
    email = Column(String, index=True , unique=True) #unique 
    password = Column(String, index=True)
    phone = Column(Integer, index=True)
    address = Column(String, index=True)
    createdat = Column(String, index=True) # datetime
    updatedat = Column(String, index=True) # datetime
    fuid = Column(String, index=True, unique=True) #
    status = Column(String, index=True, default="True") # status default value should be true
    
    def __str__(self):
        return self.username

class LoginUserModel(Base):
    __tablename__="frontend_user_token"     #frontend_user_tokens
    id = Column(Integer,primary_key=True,autoincrement=True)
    userid = Column(Integer, ForeignKey(FrontUserModel.id))
    token = Column(String, index=True)
    createdat = Column(String, index=True)
    updatedat = Column(String, index=True)
    
    def __str__(self):
        return self.token
    
class UserPostModel(Base):
    __tablename__="users_post"     # users_post
    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer, ForeignKey(FrontUserModel.id))
    title = Column(String, index=True)
    description = Column(String, index=True)
    createdat = Column(String, index=True)
    updatedat = Column(String, index=True)
    po_id = Column(String, index=True, unique=True)
    status = Column(String, index=True, default="True")