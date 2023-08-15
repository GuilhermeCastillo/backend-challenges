from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioUrl:
    def __init__(self, db: Session):
        self.db = db

    def criar(self, url: schemas.Url):
        db_url = models.Url(url=url.url)

        self.db.add(db_url)
        self.db.commit()
        self.db.refresh(db_url)

        return db_url

    def listar(self):
        urls = self.db.query(models.Url).all()
        return urls

    def obter(self):
        pass

    def remover(self):
        pass
