from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

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

@app.get("/news/", response_model=List[schemas.News])
def read_news(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    news = crud.get_new(db, skip=skip, limit=limit)
    return users


@app.get("/news/{new_id}", response_model=schemas.News)
def read_news(new_id: int, db: Session = Depends(get_db)):
    db_new = crud.get_new(db, new_id=new_id)
    if db_new is None:
        raise HTTPException(status_code=404, detail="New not found")
    return db_new



@app.get("/has_category/", response_model=List[schemas.Category])
def read_category(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    category = crud.get_category(db, skip=skip, limit=limit)
    return category
