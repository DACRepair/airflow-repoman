from airflow.models.base import Base
from sqlalchemy import Boolean, Column, DateTime, Integer, String


class Repos(Base):
    __tablename__ = "repos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    enabled = Column(Boolean, default=True)

    remote_url = Column(String(2048))
    remote_branch = Column(String(64), default='master')

    refresh = Column(Integer, default=600)
    last_updated = Column(DateTime)
