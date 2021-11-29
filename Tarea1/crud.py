from sqlalchemy.orm import Session

from . import models, schemas


def get_new(db: Session, news_id: int):
    return db.query(models.News).filter(models.News.id == news_id).first()


def get_new_by_tittle(db: Session, title: str):
    return db.query(models.News).filter(models.News.tittle == tittle).first()


def get_news(db: Session, skip: int = 0, limit: int = 100):
    return db.query(mouser_iddels.News).offset(skip).limit(limit).all()


def create_news(db: Session, new: schemas.NewsCreate):
    db_news = models.News(tittle=news.tittle)
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news


def get_category(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()


def create_new_category(db: Session, value: schemas.CategoryCreate, news_id: int):
    db_has_category = models.Category(**category.dict(), category_id=news_id)
    db.add(db_has_category)
    db.commit()
    db.refresh(db_has_category)
    return db_has_category
