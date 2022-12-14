from sqlalchemy import Boolean, Column, Float, Integer, String
from infra.sqlalchemy.config.database import Base


# modelo do nosso ORM -> representa a estrutura da db
class Produto(Base):

    __tablename__ = "produto"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    detalhes = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)


class Usuario(Base):

    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    telefone = Column(String)
    meus_produtos = Column(Float)
    minhas_vendas = Column(Boolean)
    meus_pedidos = Column(String)


class Pedido(Base):

    __tablename__ = "pedido"

    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String)
    produto = Column(String)
    quantidade = Column(Integer)
    entrega = Column(Boolean)
    endereco = Column(String)
    observacoes = Column(String)
