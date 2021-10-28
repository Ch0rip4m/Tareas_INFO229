from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base #Se importa el objeto Base desde el archivo database.py

class News(Base): 

    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    tittle = Column(String(50), unique=True)
    date = Column(String(50))
    url = Column(String(100))
    media_outlet = Column(String(50))

    #items = relationship("Item", back_populates="owner")

class Category(Base):

    __tablename__ = "has_category"

    value = Column(String(50), index=True)
    
    #owner = relationship("User", back_populates="items")
