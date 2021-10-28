from typing import List, Optional

from pydantic import BaseModel


class NewsBase(BaseModel):
    id : int
    tittle : str
    date : str
    url : str
    media_outlet : str


class NewsCreate(NewsBase):
    pass


class News(NewsBase):

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    value: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):

    class Config:
        orm_mode = True
