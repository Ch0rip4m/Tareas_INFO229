from sqlalchemy.orm import Session

from . import models, schemas


def get_new(db: Session, user_id: int):
    return db.query(models.News).filter(models.News.id == user_id).first()


def get_new(db: Session, skip: int = 0, limit: int = 100):
    return db.query(mouser_iddels.News).offset(skip).limit(limit).all()



def get_category(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()

