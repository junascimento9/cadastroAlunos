from datetime import datetime
from .config import db


class Aluno(db.Model):
    __tablename__ = 'aluno'
    cpf = db.Column('cpf', db.String(11), unique=True, nullable=False, primary_key=True)
    nome = db.Column('nome', db.String(100), nullable=True)
    data_nascimento = db.Column('data_nascimento', db.Date, nullable=True)
    sexo = db.Column('sexo', db.String(20), nullable=True)
    av1 = db.Column('av1', db.Float, nullable=True)
    av2 = db.Column('av2', db.Float, nullable=True)
    media = db.Column('media', db.Float, nullable=True)

    def __repr__(self):
        return f"Aluno(nome='{self.nome}', cpf='{self.cpf}', media={self.media})"
