from fastapi import Depends, FastAPI, Form, HTTPException, Header, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from Schema import schema
from sqlalchemy.orm import Session
from database import get_db
from Controller import controller
import sqlite3
import responseschema
import re
from Middelware.middle_ware import update_user_check
from fastapi.staticfiles import StaticFiles

app=FastAPI()

# Mount the static folder at the `/static` path
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/register-page", response_class=HTMLResponse)
async def show_form(request: Request):
    # Render the form template
    return templates.TemplateResponse("index.html", {"request": request})

# @app.post("/submit-from")
# def form_data(
#     username:str= Form(...),
#     firstname:str= Form(...),
#     lastname:str= Form(...),
#     email: str= Form(...),
#     password:str= Form(...),
#     phone: int= Form(...),
#     address:str= Form(...)
# ):
    


@app.post(
    "/register",
    response_model=responseschema.UserDetails
)
def register(
    request:schema.FrontendUser,
    sql: Session=Depends(get_db)
):
    """
    This api helps to register the user in the database.
    it take parameter request
    """
    return controller.register_user(request,sql)


@app.get(
    "/get-frontend-user",
    response_model=responseschema.UserDetails2
)
def get_front_user(
    offset: int=0,
    limit: int=10,
    sql: Session=Depends(get_db)
):
    """ 
    
    """
    return controller.get_user(offset,limit,sql)
    

@app.delete(
    "/delete",
    response_model=responseschema.UserDelete
)
def delete_front_user(
    # request: schema.FrontendUser,
    username:str,
    sql: Session=Depends(get_db)
):
    return controller.delete_user(username,sql)


@app.post(
    "/login",
    response_model=responseschema.UserDetails
)
def login_front_user(
    request: schema.Login,
    sql:Session=Depends(get_db)
):
    return controller.login_user(request,sql)


@app.delete(
    "/logout"
)
def logout_user(
    username:str,
    sql:Session=Depends(get_db)
):
    return controller.logout_users(username,sql)


@app.get(
    "/get-frontend-user-details",
    response_model=responseschema.User
)
def frontend_user_details(

    fuid : str,
    sql:Session=Depends(get_db)
):
    return controller.get_user_details(fuid,sql)


@app.post(
    "/update-user",
    response_model=responseschema.UpdatedUserDetail
)
def update_front_user(
    request : schema.UpdateUser,
    sql : Session=Depends(get_db),
):
    # update_user_check(request,sql)
    return controller.update_user(request,sql)


@app.post(
    "/add-post",
    response_model=responseschema.UserPostRS
)
def add_post(
    request : schema.UserPost,
    sql : Session=Depends(get_db),
    header: str = Header("Default Value")
):
    if header == "Default Value":
        raise HTTPException(status_code=400, detail="Header is required")

    return controller.add_user_post(request,sql,header)


@app.get(
    "/get-post",
    response_model=responseschema.GetUserPost
)
def get_post(
    offset : int=0,
    limit : int=10,
    sql : Session=Depends(get_db),
    header: str = Header()
):
    if header == "":
        raise HTTPException(status_code=400, detail="Header is required")

    return controller.get_user_post(offset,limit,sql,header)


@app.delete(
    "/delete-post",
    response_model=responseschema.UserPostRS
)
def delete_post(
    post_id : str,
    sql: Session=Depends(get_db),
    header : str=Header()
):
    if header =="":
        raise HTTPException (status_code=400,detail="Header is required")
    
    return controller.delete_user_post(post_id,sql,header)


@app.post(
    "/update-post",
    response_model=responseschema.UserPostRS
)
def update_post(
    post_id : str,
    title : str,
    description : str,
# hello how are you
    sql : Session=Depends(get_db),
    header : str=Header()
):
    if header=="":
        raise HTTPException (status_code=400,detail="Header is required")

    return controller.update_user_post(post_id,title,description,sql,header)
