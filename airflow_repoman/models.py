from airflow.models.base import Base
from sqlalchemy import Column, Integer


class Repos(Base):
    __tablename__ = "repos"
    test = Column(Integer, primary_key=True, autoincrement=True)
