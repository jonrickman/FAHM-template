from fastapi import FastAPI
from fahm_template.routers import generic_router, user_router
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(generic_router)
app.include_router(user_router)
