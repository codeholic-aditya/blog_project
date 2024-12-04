import re
from fastapi import HTTPException
from sqlalchemy.orm import Session
from Schema import schema
from Model.frontendusermodel import (
    FrontUserModel,
    LoginUserModel,
    UserPostModel
)
from dependencies import (
    generate_uuid,
    hash_convertor,
    hash_generator,
    validation
)
import datetime
from dependencies import auth_token
from responseschema import UserPostRS

# from Middelware.middle_ware import update_user_check


def register_user(
    request: schema.FrontendUser,
    sql: Session
):
    """
    This function is used to register the user who is not present in the database
    """
    
    isRegister =sql.query(FrontUserModel).filter(
    FrontUserModel.username == request.username
    ).first()
    
    
    if isRegister:
        
        if isRegister.username == request.username:
            return {"message": "User already exists"}
        
        
    else:
        if not validation.email_validation_check(request.email):
            return {"message":"Email is not valid"}
        
        
        if not validation.phone_validation_check(request.phone):
            return {"message":"Phone is not valid"}
        
        # Validate fields
        
        if not request.username.strip():
            return {"message": "Username is invalid"}
        
        if not request.password.strip():
            return {"message": "Password is invalid"}
        
        
        # Create a new user instance
        new_user = FrontUserModel(
            username=request.username,
            firstname=request.first_name,  
            lastname=request.last_name,  
            email=request.email,
            password=hash_generator(request.password),
            phone=request.phone,
            address=request.address,
            createdat=str(datetime.datetime.now()),
            updatedat=str(datetime.datetime.now()),
            fuid=generate_uuid()
        )
        
        sql.add(new_user)
        sql.commit()
        sql.refresh(new_user)

        return {
            "user":new_user,
            "message":"User register successfully"
            }


def get_user(
    offset:int,
    limit:int,
    sql:Session
):
    """ 
    This function use to get the details of the user which are active
    """
    showAllUser=sql.query(
        FrontUserModel
        ).filter(
            FrontUserModel.status=="True"
        ).offset(offset).limit(limit).all()

    count=sql.query(FrontUserModel).count()


    return {
        "user": showAllUser,
        "total": count
        }


def delete_user(
    username: str,
    sql: Session
):
    """
    This function is used for deactivate the user
    """
    
    user_del=sql.query(FrontUserModel).filter(username==FrontUserModel.username).first()

    if user_del:
        user_del.status="False"
    else:
        return {"message": "User not found"}
    
    sql.commit()
    sql.refresh(user_del)
    
    return {"user": user_del}


def login_user(
    request:schema.Login,
    sql:Session
):
    """
    This function is used to login the user if he is already register
    """
    
    if not request.username.strip():
        return {"message": "Username is invalid"}

    if not request.password.strip():
        return {"message": "Password is invalid"}

    if validation.email_validation_check(request.username):
        isUserExists=sql.query(
            FrontUserModel
        ).filter(
            FrontUserModel.email==request.username
        ).first()
    else:
        isUserExists=sql.query(
            FrontUserModel
        ).filter(
            FrontUserModel.username==request.username
        ).first()
    
    
    if isUserExists:
        
        if isUserExists.status=="False":
            return {"message":"User not found"}
        
        get_password=hash_convertor(isUserExists.password)

        if not get_password==request.password:
            return {"message":"password incorrect"}

        login_table=sql.query(LoginUserModel).filter(isUserExists.id==LoginUserModel.userid).first()

        if login_table:
            login_table.token=generate_uuid()
            login_table.updatedat=str(datetime.datetime.now())
            sql.commit()
        else:
            
            loginuser = LoginUserModel(
                userid=isUserExists.id,
                token = generate_uuid(),
                createdat = str(datetime.datetime.now()),
                updatedat = str(datetime.datetime.now()),
            )
            sql.add(loginuser)
            sql.commit()
            sql.refresh(loginuser)

        return {"message":"User logined successfully"}

    else:
        return {"message":"User is not found"}


def logout_users(
    username : str,
    sql : Session
):
    """
    This function is used to logout the user
    """
    
    if not username.strip():
        return {"message": "Username is invalid"}

    logout_user_id = sql.query(FrontUserModel).filter(FrontUserModel.username==username).first()
    print(logout_user_id)
    
    if not logout_user_id:
        return {"message": "User not found"}
    
    xx=logout_user_id.id
    
    logout_user = sql.query(LoginUserModel).filter(xx==LoginUserModel.userid).first()
    print(logout_user)
    
    if logout_user:
        sql.delete(logout_user)
        sql.commit()
        return {"message":"User logout successfully"}
        
    else:
        return {"message":"User already logout"}
    
        
def get_user_details(

    fuid:str,
    sql:Session
):
    """
    This function is used to get the single user details
    """
    
    if not fuid.strip():
        return {"Message":"User not found"}
    
    else:
        user_exists=sql.query(FrontUserModel).filter(FrontUserModel.fuid==fuid).first()
        
        if user_exists:
            return {"user" : user_exists}
        
        else:
            return {"Message":"User not found"}
        
        
def update_user(
    request : schema.UpdateUser,
    sql : Session
):
    if not request.username.strip():
        return {"message":"Username is invalid"}
       

    userRow=sql.query(FrontUserModel).filter(FrontUserModel.username==request.username).first()

    if userRow:
        print(type(userRow))
        if request.first_name:
            userRow.firstname=request.first_name
            
        if request.last_name:
            userRow.lastname=request.last_name
            
        if request.email:
            validation.email_validation_check(request.email)
            userRow.email=request.email
            
        if request.phone:
            validation.phone_validation_check(request.phone)
            userRow.phone=request.phone
            
        if request.address:
            userRow.address=request.address
        
        userRow.updatedat=datetime.datetime.now()
            
        sql.commit()
        
        return {"message": userRow}
    else :
        return {"message":"User not found"}


def add_user_post(
    request : schema.UserPost,
    sql : Session,
    header:str
):
    tokens=auth_token(header,sql)
    
    
    if header != tokens:
        raise HTTPException(status_code=401, detail="Unauthorized")

    is_user=sql.query(LoginUserModel).filter(LoginUserModel.token==header).first()

    if is_user:
        user_post=UserPostModel(
            user_id=is_user.id,
            title=request.title,
            description=request.description,
            createdat=datetime.datetime.now(),
            updatedat=datetime.datetime.now(),
            po_id=generate_uuid()
        )
        sql.add(user_post)
        sql.commit()
        
        return {
            "title":user_post.title,
            "description":user_post.description
            }
    else:
        return {"message":"Please login first!!"}


def get_user_post(
    offset : int,
    limit : int,
    sql : Session,
    header:str
):
    tokens=auth_token(header,sql)
    
    if header != tokens:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    is_user=sql.query(LoginUserModel).filter(LoginUserModel.token==header).first()

    if is_user:
        showAllPost=sql.query(UserPostModel).filter(UserPostModel.user_id==is_user.id).offset(offset).limit(limit).all()
        count=sql.query(UserPostModel).filter(UserPostModel.user_id==is_user.id).all()
        
        posts_data = []

        # Loop through the posts and append the relevant details to the list
        for post in showAllPost:
            posts_data.append({
                "title": post.title,
                "description": post.description,
                "created_at": post.createdat,
                "updated_at": post.updatedat
        })
            
        return {
            "users_post": posts_data,
            "total": len(count)
        }


def delete_user_post(
    post_id : str,
    sql : Session,
    header:str
):
    tokens=auth_token(header,sql)
    
    if header != tokens:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    is_user=sql.query(LoginUserModel).filter(LoginUserModel.token==header).first()

    if not is_user:
        raise HTTPException(status_code=401, detail="Unauthorized")

    delete_post = sql.query(
        UserPostModel
        ).filter_by(
            po_id = post_id,
            status="True"
            ).first()

    if not delete_post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    delete_post.status="False"
    
    sql.commit()

    return {
        "title": delete_post.title,
        "description": delete_post.description
    }
    
    
def update_user_post(
    post_id : str,
    title : str,
    description : str,
    sql : Session,
    header : str
):
    token=auth_token(header,sql)
    
    if header!=token:
        raise HTTPException(status_code=401,detail="Unauthorized")

    post_update=sql.query(
        UserPostModel
        ).filter_by(
            po_id=post_id,
            status="True"
            ).first()
    
    if not post_update:
        raise HTTPException(status_code=401,detail="Unauthorized")
    
    post_update.title=title
    post_update.description=description
    post_update.updatedat=datetime.datetime.now()
    
    sql.commit()


    return {
        "title": post_update.title,
        "description": post_update.description
    }
    
    
    
    # this is changes