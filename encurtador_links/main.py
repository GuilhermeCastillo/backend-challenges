from fastapi import FastAPI, Depends
from src.schemas.schemas import Url
from src.infra.sqlalchemy.repositorio.url import RepositorioUrl
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.services.service_encurtar_url import generate_random_string

criar_bd()

app = FastAPI()


@app.post("/encurtar-url")
async def encurtar_url(url: Url, db: Session = Depends(get_db)):
    url_encurtada = generate_random_string()
    response = RepositorioUrl(db).criar(url, url_encurtada)

    return response

@app.get("/urls")
async def urls(db: Session = Depends(get_db)):
    get_all_urls = RepositorioUrl(db).listar()
    
    return get_all_urls