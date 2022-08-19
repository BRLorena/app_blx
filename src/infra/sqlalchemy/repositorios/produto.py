from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models
from src.schemas import schemas


class RepositorioProduto():

  def __init__(self, db:Session):
    self.db = db

# chamei a class produto P/ converter schema em modelo P/ o DB
  def criar(self, produto: schemas.Produto):
    db_produto = models.Produto(nome=produto.nome,
    detalhes = produto.detalhes, preco = produto.preco,
    disponivel = produto.disponivel )
    self.db.add(db_produto) # add ao bd
    self.db.commit() # confirma 
    self.db.refresh(db_produto) # atualiza
    return db_produto #retorna os dados

  def listar(self):
    produtos = self.db.query(models.Produto).all()
    return produtos

  def obter(self):
    pass

  def remover(self):
    pass
