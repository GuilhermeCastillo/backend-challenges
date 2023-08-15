from sqlalchemy import Column, Integer, String
from src.infra.sqlalchemy.config.database import Base


class Url(Base):
    __tablename__ = "url"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String)
    url_encurtada = Column(String)
