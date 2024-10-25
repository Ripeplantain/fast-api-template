from fastapi import FastAPI
from src.controllers import users_ct
app = FastAPI()

app.include_router(users_ct.router)