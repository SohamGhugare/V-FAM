from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


""" 
    Linking models 
        - UserGroupLink: linkage between user and group relationship.    
"""

class UserGroupLink(SQLModel, table=True):
    user_id: Optional[int] = Field(
        default=None, foreign_key="group.id", primary_key=True
    )
    group_id: Optional[int] = Field(
        default=None, foreign_key="user.id", primary_key=True
    )

""" 
    Main models 
        - User model: populates all the user data
        - Group model: populates all the group data
        - Showcase model: (non-tabular) has all the showcase settings

"""

class User(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    username: str = Field(max_length=15)
    bio: Optional[str] = Field(max_length=255, default=None)
    password: str
    groups: List["Group"] = Relationship(back_populates="teammates", link_model=UserGroupLink)
    showcase_id: Optional[int] = Field(foreign_key="showcase.id")

class Group(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    title: str = Field(max_length = 50)
    description: str
    teammates: List["User"] = Relationship(back_populates="groups", link_model=UserGroupLink)
    tags = list


class Showcase(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    enabled: bool = Field(default=False)
    items: List["ShowcaseItem"] = Relationship(back_populates="showcase")

class ShowcaseItem(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    title: str
    description: str
    showcase: Optional[Showcase] = Relationship(back_populates="items")
    



