from uuid import uuid4

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware  # permitir front usar API
from schemas.schemas import Produto, Usuario  # import class Produto from schemas
from infra.sqlalchemy.repositorios.produto import RepositorioProduto
from infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from sqlalchemy.orm import Session
from infra.sqlalchemy.config.database import get_db, criar_bd

# Criar bd
criar_bd()

# start APP
app = FastAPI()

# permissions
# origins = ["http://127.0.0.1:5500"]

# # cadastrar os interceptors (middleware) permite CORS p/ algumas requests
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

## ______________________________ Produtos __________________________________________________________
@app.post("/produtos")  # Constructor RepositorioProduto precisa de um db
def criar_produtos(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


## common
@app.get("/produtos", status_code=200)
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos


## ____________________________________Usuario__________________________________________________________________
@app.post("/usuarios", status_code=200)
def criar_usuarios(usuario: Usuario, db: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado


@app.get("/usuarios", status_code=200)
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios


# @app.get("/animal/{id_animal}")
# async def getAnimal(id_animal: str):
#     for animal in db:
#         if animal.id == id_animal:
#             return {"mensagem": f"O id do {animal.name} é {id_animal}"}
#     return {"mensagem": "Animal not found"}


# @app.post("/animal")
# async def create_animal(animal: Animal):
#     animal.id = str(uuid4())  # gerar id automatico -> cast to str
#     db.append(animal)
#     return {"Animal ": f" {animal.name} cadastrado com sucesso"}


# @app.delete("/animal/{id_animal}")
# async def remove_animal(id_animal: str):
#     posicao_animal = -1
#     for i, animal in enumerate(db):
#         if animal.id == id_animal:
#             posicao_animal = i
#             break  # encontrou posso parar
#     if posicao_animal != -1:
#         db.pop(posicao_animal)
#         return {"mensagem": "Animal removido com sucesso"}
#     else:
#         return {"mensagem ": f"Animal não localizado"}
