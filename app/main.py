from fastapi import FastAPI
from starlette_admin import CustomView
from starlette_admin.contrib.sqlmodel import Admin, ModelView
from authlib.integrations.starlette_client import OAuth

from app.core.database import engine
from app.core.config import settings
from app.auth_provider import MyAuthProvider
from app.models import User

app = FastAPI(title="FastAPI Admin Template")

# Create admin interface
admin = Admin(
    engine,
    title="FastAPI Admin Template",
    base_url="/admin",
    route_name="admin",
    statics_dir="statics/admin",
    templates_dir="templates/admin",
    logo_url="https://preview.tabler.io/static/logo-white.svg",
    login_logo_url="https://preview.tabler.io/static/logo.svg",
    index_view=CustomView(label="Home", icon="fa fa-home", path="/home", template_path="home.html"),
    auth_provider=MyAuthProvider(login_path="/sign-in", logout_path="/sign-out"),
    middlewares=[],
    debug=settings.DEBUG,
)

# Add modell views
# admin.add_view(ModelView(User))

# Mount admin interface
admin.mount_to(app)


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
