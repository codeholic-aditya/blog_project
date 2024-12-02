from pydantic import BaseModel
from typing import Optional

class FrontendUser(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    phone: int
    address: str
    
    
class UserPost(BaseModel):
    title : str
    description : str
    # createdat : str
    # updatedat : str
    # po_id : str
    # status : str

    
class Login(BaseModel):
    username : str
    password : str

class UpdateUser(BaseModel):
    username :Optional[str] = None
    first_name : Optional[str] = None
    last_name : Optional[str] = None
    email : Optional[str] = None
    phone : Optional[int] = None
    address : Optional[str] = None
    # updated_at : Optional[str] = None