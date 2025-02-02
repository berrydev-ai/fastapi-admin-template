from fastapi import FastAPI
from starlette_admin import CustomView
from starlette_admin.contrib.sqlmodel import Admin, ModelView
from authlib.integrations.starlette_client import OAuth

from app.core.database import engine
from app.core.config import settings
from app.auth_provider import MyAuthProvider
from app.models import User

app = FastAPI(title="FastAPI Admin Template")



# Mount admin interface
admin.mount_to(app)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}