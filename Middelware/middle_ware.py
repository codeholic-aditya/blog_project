from sqlalchemy.orm import Session
from Model.frontendusermodel import FrontUserModel
from dependencies import validation
from Schema import schema


def update_user_check(
    request : schema.UpdateUser,
    sql : Session
):
    
    if not request.username.strip():
        return {"message":"Username is invalid"}
    
    if not request.password.strip():
        return {"message": "Password is invalid"}
    
    validation.phone_validation_check(request.phone)
    print(type(request.phone))
    
    if validation.email_validation_check(request.email):
        userRow=sql.query(FrontUserModel).filter(FrontUserModel.email==request.email).first()
       
        if userRow:
            return userRow.fuid
        else:
            return {"message":"User not found"}

    else:
        userRow=sql.query(FrontUserModel).filter(FrontUserModel.username==request.username).first()
        if userRow:
            return userRow.fuid
        else:
            return {"message":"User not found"}

    
    
    