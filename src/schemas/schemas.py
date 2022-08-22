from typing import List, Optional

from pydantic import BaseModel


class Produto(BaseModel):
    id: Optional[str] = None
    # usuario:Usuario
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    # foto: any


class Pedido(BaseModel):
    id: Optional[str] = None
    # usuario: Usuario
    # produto: str
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = "Sem observações"


class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    # meus_produtos = List[Produto]
    # minhas_vendas: List[Pedido]
    # meus_pedidos: List[Pedido]

    # Class interna - esta dentro da class Produto
    class Config:
        orm_mode = True
