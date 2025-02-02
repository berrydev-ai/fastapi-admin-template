from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    auth0_id: str = Field(index=True, unique=True)
    email: str = Field(index=True)
    username: str = Field(index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = Field(default=True)
    
    # Optional but commonly useful fields
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    picture_url: Optional[str] = None
    last_login: Optional[datetime] = None

    def __str__(self) -> str:
        return self.email