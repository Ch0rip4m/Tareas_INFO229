from typing import List, Optional

from pydantic import BaseModel


class CategoryBase(BaseModel):
    value: str

class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    category_id: int

    class Config:
        orm_mode = True


class NewsBase(BaseModel):
    title: str
    data: str 
    url: str
    media_outlet: str 


class NewsCreate(NewsBase):
    pass


class News(NewsBase):
    id: int

    class Config:
        orm_mode = True
