from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base #Se importa el objeto Base desde el archivo database.py

class News(Base): 

    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    tittle = Column(String(50), unique=False, index=False)
    date = Column(Date(), index=False)
    url = Column(String(50), index=False)
    media_outlet = Column(String(50), index=False)
    category = Column(String(50), index=False)

    
