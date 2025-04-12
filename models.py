from typing import Optional
from sqlmodel import Field, SQLModel

class Welcome(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    welcome_text: str