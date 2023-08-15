from fastapi import FastAPI, Depends
from src.schemas.schemas import Url
from src.infra.sqlalchemy.repositorio.url import RepositorioUrl
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db, criar_bd


criar_bd()

app = FastAPI()


@app.post("/encurtar-url")
async def encutar_url(url: Url, db: Session = Depends(get_db)):
    url_encurtada = RepositorioUrl(db).criar(url)

    return url_encurtada

@app.get("/urls")
async def urls():
    return {"message": "Hello World"}