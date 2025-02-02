from fastapi import FastAPI
from starlette_admin import CustomView
from starlette_admin.contrib.sqlmodel import Admin, ModelView
from authlib.integrations.starlette_client import OAuth

from app.core.database import engine
from app.core.config import settings
from app.auth_provider import MyAuthProvider
from app.models import User

from starlette_admin import CustomView
from starlette.requests import Request
from starlette.responses import Response
from sqlmodel import select

# Create admin interface
admin = Admin(
    engine,
    title="FastAPI Admin Template",
    base_url="/admin",
    route_name="admin",
    statics_dir="app/statics/admin",
    templates_dir="app/templates/admin",
    logo_url="/admin/static/img/logo.svg",
    login_logo_url="/admin/static/img/logo.svg",
    index_view=CustomView(label="Home", icon="fa fa-home", path="/home", template_path="home.html"),
    auth_provider=MyAuthProvider(login_path="/sign-in", logout_path="/sign-out"),
    middlewares=[],
    debug=settings.DEBUG,
)

# Add User model to admin with custom configuration
class UserAdmin(ModelView):
    model = User
    icon = "fa fa-users"
    name = "Users"
    name_plural = "Users"
    
    # Customize which columns appear in the list view
    column_list = [User.id, User.email, User.username, User.is_active, User.created_at]
    
    # Make certain fields readonly
    form_excluded_columns = ["auth0_id", "created_at", "last_login"]
    
    # Add search functionality
    column_searchable_list = [User.email, User.username]
    
    # Add filters
    column_filters = [User.is_active, User.created_at]
    
    # Customize sorting
    column_default_sort = ("created_at", True)  # Sort by created_at descending

admin.add_view(UserAdmin)

class AdminHomeView(CustomView):
    template_path = "home.html"
    
    async def render(self, request: Request) -> Response:
        # Get some stats for the dashboard
        async with request.state.session as session:
            user_count = session.exec(select(func.count(User.id))).one()
            
        context = {
            "user_count": user_count,
            # Add more context data as needed
        }
        return await super().render(request, context)
