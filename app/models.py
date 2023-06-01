from app import db
class Aluno:     
    def __init__(self, id, cpf, nome, data_nascimento, sexo, idade, av1, av2, media):         
        self.id = id         
        self.cpf = cpf         
        self.nome = nome         
        self.data_nascimento = data_nascimento         
        self.sexo = sexo         
        self.idade = idade         
        self.av1 = av1         
        self.av2 = av2         
        self.media = media