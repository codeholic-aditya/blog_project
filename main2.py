from fastapi import Depends, FastAPI, Form
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app=FastAPI()

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    # Render the form template
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit")
async def submit_form(name: str = Form(...), email: str = Form(...)):
    # Process the submitted form data
    return {"message": "Form submitted successfully!", "name": name, "email": email}