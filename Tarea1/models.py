from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base #Se importa el objeto Base desde el archivo database.py

class News(Base): 

    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    tittle = Column(String(50), unique=True, index=True)
    data = Column(String(50))
    url = Column(String(50))
    media_outlet = Column(String(50))

    relationCat = relationship("Category", back_populates="relationNews")

class Category(Base):

    __tablename__ = "has_category"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(String(50))
    category_id = Column(Integer, ForeignKey("news.id"))

    relationNews = relationship("News", back_populates="relationCat")
