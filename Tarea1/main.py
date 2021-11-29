from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return RedirectResponse(url = "/docs/")


@app.post("/news/", response_model=schemas.News)
def create_news(news: schemas.NewsCreate, db: Session = Depends(get_db)):
    db_news = crud.get_new_by_tittle(db, tittle=news.tittle)
    if db_news:
        raise HTTPException(status_code=400, detail="tittle already registered")
    return crud.create_news(db=db, news=news)


@app.get("/news/", response_model=List[schemas.News])
def read_news(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    news = crud.get_news(db, skip=skip, limit=limit)
    return news


@app.get("/news/{news_id}", response_model=schemas.News)
def read_news(news_id: int, db: Session = Depends(get_db)):
    db_news = crud.get_new(db, news_id=news_id)
    if db_news is None:
        raise HTTPException(status_code=404, detail="news not found")
    return db_news


@app.post("/news/{news_id}/has_category/", response_model=schemas.Category)
def create_category_for_news(
    news_id: int, category: schemas.CategoryCreate, db: Session = Depends(get_db)
):
    return crud.create_new_category(db=db, category=category, news_id=news_id)


@app.get("/has_category/", response_model=List[schemas.Category])
def read_categorys(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categorys = crud.get_category(db, skip=skip, limit=limit)
    return categorys
