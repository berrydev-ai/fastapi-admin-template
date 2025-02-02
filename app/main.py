from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from starlette_admin.contrib.sqlmodel import Admin, ModelView

from app.core.config import settings
from app.core.database import engine
from app.models import User

app = FastAPI(title="FastAPI Admin Template")

# Add session middleware
app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

# Create admin interface
admin = Admin(engine, title="Admin Interface")

# Add views
admin.add_view(ModelView(User))

# Mount admin interface
admin.mount_to(app)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
