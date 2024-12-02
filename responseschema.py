
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class User(BaseModel):
    username:str
    email: str
    phone: int
    createdat: str
    updatedat: str
    
    
class UserDetails(BaseModel):           # for create user
    user:Optional[User]=None
    message:Optional[str]=None
    
class UserDetails2(BaseModel):          # for get the user details
    user:Optional[list[User]]=None
    message:Optional[str]=None



class UserDeactivate(BaseModel):
    username:str
    email:str
    
class UserDelete(BaseModel):        # to deactivate the user
    user : Optional[UserDeactivate]=None
    message : Optional[str]=None

class UpdatedUserDetail(BaseModel):
    username :Optional[str] = None
    first_name : Optional[str] = None
    last_name : Optional[str] = None
    email : Optional[str] = None
    phone : Optional[int] = None
    updatedat : Optional[str] = None

class UserPostRS(BaseModel):
    title : str
    description : str