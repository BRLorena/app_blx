from sqlalchemy.orm import Session
from infra.sqlalchemy.models import models
from schemas import schemas


class RepositorioUsuario:
    def __init__(self, db: Session):
        self.db = db

    # chamei a class usuario P/ converter schema em modelo P/ o DB
    def criar(self, usuario: schemas.Usuario):
        db_usuario = models.Usuario(
            nome=usuario.nome,
            telefone=usuario.telefone,
        )
        self.db.add(db_usuario)  # add ao bd
        self.db.commit()  # confirma
        self.db.refresh(db_usuario)  # atualiza
        return db_usuario  # retorna os dados

    def listar(self):
        usuarios = self.db.query(models.Usuario).all()
        return usuarios

    def obter(self):
        pass

    def remover(self):
        pass
