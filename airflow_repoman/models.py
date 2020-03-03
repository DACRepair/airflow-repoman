import datetime
from airflow.exceptions import AirflowException
from airflow.models.base import Base
from airflow.models.crypto import get_fernet
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import synonym


class Repos(Base):
    __tablename__ = "repoman_repos"
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(255))
    enabled = Column(Boolean, default=True)

    remote_url = Column(String(2048), nullable=False)
    remote_branch = Column(String(64), default='master')

    remote_user = Column(String(5000), default=None, nullable=True)
    _remote_pass = Column('remote_pass', String(5000))

    refresh = Column(Integer, default=600)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow())

    is_encrypted = Column(Boolean, unique=False, default=False)

    def __init__(self, name: str = None, enabled: bool = True, remote_url: str = None, remote_branch: str = 'master',
                 remote_user: str = None, remote_pass: str = None, refresh: int = None,
                 last_updated: datetime.datetime = datetime.datetime.utcnow()):
        self.name = name
        self.enabled = enabled
        self.remote_url = remote_url
        self.remote_branch = remote_branch
        self.remote_user = remote_user
        self.remote_pass = remote_pass
        self.refresh = refresh
        self.last_updated = last_updated

    def get_password(self):
        if self._remote_pass and self.is_encrypted:
            fernet = get_fernet()
            if not fernet.is_encrypted:
                raise AirflowException(
                    "Can't decrypt encrypted password for login={}, \
                    FERNET_KEY configuration is missing".format(self.remote_user))
            return fernet.decrypt(bytes(self._remote_pass, 'utf-8')).decode()
        else:
            return self._remote_pass

    def set_password(self, value):
        if value:
            fernet = get_fernet()
            self._remote_pass = fernet.encrypt(bytes(value, 'utf-8')).decode()
            self.is_encrypted = fernet.is_encrypted

    @declared_attr
    def remote_pass(cls):
        return synonym('_remote_pass',
                       descriptor=property(cls.get_password, cls.set_password))
