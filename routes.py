from flask import Blueprint, render_template, request, redirect, flash, jsonify
from datetime import date
from .models import Aluno
from .config import app, db

app_blueprint = Blueprint('app', __name__)

alunos = []


@app_blueprint.route('/')
def index():
    alunos = Aluno.query.all()
    return render_template('index.html', alunos=alunos)


@app_blueprint.route('/add', methods=['POST'])
def add():
    data = request.json
    
    cpf = data.get('cpf')
    
    # verificar se o CPF já está cadastrado
    aluno_existe = Aluno.query.filter_by(cpf=cpf).first()
    if aluno_existe:
        return jsonify({'message': 'CPF já cadastrado!'})
        
    
    nome = data.get('nome')
    data_nascimento = data.get('data_nascimento')
    sexo = data.get('sexo')
    av1 = float(data.get('av1'))
    av2 = float(data.get('av2'))
    media = (av1 + av2) / 2

    aluno = Aluno(cpf=cpf, nome=nome, data_nascimento=data_nascimento,
                  sexo=sexo, av1=av1, av2=av2, media=media)
    db.session.add(aluno)
    db.session.commit()

    return jsonify({'message': 'Aluno cadastrado com sucesso!'})


@app_blueprint.route('/delete/<cpf>', methods=['DELETE'])
def delete(cpf):
    aluno = Aluno.query.filter_by(cpf=cpf).first()
    if aluno:
        db.session.delete(aluno)
        db.session.commit()
        return jsonify({'message': 'Aluno removido com sucesso.'}), 200
    else:
        return jsonify({'error': 'Aluno não encontrado.'}), 404


@app_blueprint.route('/edit/<cpf>', methods=['PUT'])
def edit(cpf):
    aluno = Aluno.query.filter_by(cpf=cpf).first()

    if not aluno:
        return jsonify({'error': 'Aluno não encontrado!'}), 404

    if request.method == 'PUT':
        data = request.json

        if not data:
            return jsonify({'error': 'Dados inválidos'}), 404
        
        aluno.data_nascimento = data.get('data_nascimento')
        aluno.sexo = data.get('sexo')
        aluno.av1 = float(data.get('av1'))
        aluno.av2 = float(data.get('av2'))
        aluno.media = (aluno.av1 + aluno.av2) / 2

        db.session.commit()

        return jsonify({'message': 'Informações do aluno atualizadas com sucesso!'}), 200
