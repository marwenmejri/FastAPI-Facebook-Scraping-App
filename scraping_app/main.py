from .scraping.post_scraper import Scrap
from .models.post import Post
from .database import init_db, get_db
from .schemas.post_schema import PostSchema, PostCreate, ScrapingRequest

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from typing import List

app = FastAPI()
app.mount("/scraping_app/static", StaticFiles(directory="scraping_app/static"), name="scraping_app/static")


@app.on_event("startup")
def startup_event():
    init_db()


@app.get("/")
async def home():
    return FileResponse('scraping_app/static/html/index.html')


@app.get("/posts/", response_model=List[PostSchema])
def list_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return posts


@app.get("/posts/page/{page_name}", response_model=List[PostSchema])
def get_post_by_page_name(page_name: str, db: Session = Depends(get_db)):
    posts = db.query(Post).filter(Post.page == page_name).all()
    if not posts:
        raise HTTPException(status_code=404, detail="Posts not found")
    return posts


@app.get("/posts/id/{post_id}", response_model=PostSchema)
def get_post_by_id(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == int(post_id)).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@app.post("/scrape/", response_model=List[PostSchema])
def scrape_and_save_posts(scraping_request: ScrapingRequest, db: Session = Depends(get_db)):
    scraper = Scrap(url=scraping_request.url)
    scraped_posts = scraper.scrap_data()
    saved_posts = []
    for post_data in scraped_posts:
        post_create = PostCreate(**post_data)
        post = Post(**post_create.dict())
        db.add(post)
        try:
            db.commit()
            db.refresh(post)
            saved_posts.append(post)
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=400, detail=f"Failed to add post: {e}")
    return saved_posts
