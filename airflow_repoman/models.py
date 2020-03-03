import datetime
from airflow.models.base import Base
from airflow.settings import conf
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy_utils import EncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import FernetEngine


class Repos(Base):
    __tablename__ = "repoman_repos"
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(255))
    enabled = Column(Boolean, default=True)

    remote_url = Column(String(2048), nullable=False)
    remote_branch = Column(String(64), default='master')

    remote_user = Column(String(5000), default=None, nullable=True)
    remote_pass = Column(EncryptedType(String(5000), conf.get('core', 'fernet_key', fallback=None), FernetEngine))

    refresh = Column(Integer, default=600)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow())
