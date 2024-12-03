
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

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
    title : Optional[str] = None
    description : Optional[str] = None
    
class GetPostDetails(BaseModel):
    title : str 
    description : str 
    created_at : str
    updated_at : str 


class GetUserPost(BaseModel):
    users_post : Optional[list[GetPostDetails]]
    total : Optional[int] = None
    
    
# class UpdatePost(BaseModel):
#     user_post : Optional[list]