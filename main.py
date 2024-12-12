from fastapi import Depends, FastAPI, Form, HTTPException, Header, Request,status
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
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/login-page", response_class=HTMLResponse)
async def show_form(request: Request):
    # Render the form template
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    # Render the form template
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/blog-add", response_class=HTMLResponse)
async def show_form(request: Request):
    # Render the form template
    return templates.TemplateResponse("blog_add.html", {"request": request})


@app.post(
    "/register",
    response_model=responseschema.UserDetails,
    status_code=status.HTTP_201_CREATED
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
    response_model=responseschema.UserDetails2,
    status_code=status.HTTP_200_OK
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
    response_model=responseschema.UserDelete,
    status_code=status.HTTP_200_OK
)
def delete_front_user(
    # request: schema.FrontendUser,
    username:str,
    sql: Session=Depends(get_db)
):
    return controller.delete_user(username,sql)


@app.post(
    "/login",
    response_model=responseschema.LoginSchema,
    status_code=status.HTTP_200_OK
)
def login_front_user(
    request: schema.Login,
    sql:Session=Depends(get_db)
):
    return controller.login_user(request,sql)


@app.delete(
    "/logout",
    status_code=status.HTTP_200_OK
)
def logout_user(
    header:str=Header(),
    sql:Session=Depends(get_db)
):
    if header =="":
        raise HTTPException (status_code=400,detail="Header is required")
    return controller.logout_users(header,sql)


@app.get(
    "/get-frontend-user-details",
    response_model=responseschema.UserDetails3,
    status_code=status.HTTP_200_OK
)
def frontend_user_details(

    header : str,
    sql:Session=Depends(get_db)
):
    return controller.get_user_details(header,sql)


@app.post(
    "/update-user",
    response_model=responseschema.UpdatedUserDetail,
    status_code=status.HTTP_200_OK
)
def update_front_user(
    request : schema.UpdateUser,
    sql : Session=Depends(get_db),
):
    # update_user_check(request,sql)
    return controller.update_user(request,sql)


@app.post(
    "/add-post",
    response_model=responseschema.UserPostRS,
    status_code=status.HTTP_201_CREATED
)
def add_post(
    request : schema.UserPost,
    sql : Session=Depends(get_db),
    header: str = Header("")
):
    if header == "":
        raise HTTPException(status_code=400, detail="Header is required")

    return controller.add_user_post(request,sql,header)


@app.get(
    "/get-post",
    response_model=responseschema.GetUserPost,
    status_code=status.HTTP_200_OK
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
    response_model=responseschema.UserPostRS,
    status_code=status.HTTP_200_OK
)
def delete_post(
    title : str,
    sql: Session=Depends(get_db),
    header : str=Header()
):
    if header =="":
        raise HTTPException (status_code=400,detail="Header is required")
    
    return controller.delete_user_post(title,sql,header)


@app.post(
    "/update-post",
    response_model=responseschema.UserPostRS,
    status_code=status.HTTP_200_OK
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
