from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    page = Column(String)
    url = Column(String, unique=True)
    text = Column(String)
    date = Column(DateTime)
    nbr_emojis = Column(String)
    nbr_comments = Column(String)
    __table_args__ = (UniqueConstraint('page', 'url', name='_page_url_uc'),)
