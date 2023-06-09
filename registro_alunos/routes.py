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
        jsonify({'error': 'Aluno não encontrado!'}), 404
        return redirect('/')

    if request.method == 'PUT':
        data = request.json

        if not data:
            jsonify({'error': 'Dados inválidos'}), 404
            return redirect('/')

        aluno.cpf = data.get('cpf')
        aluno.nome = data.get('nome')
        aluno.data_nascimento = data.get('data_nascimento')
        aluno.sexo = data.get('sexo')
        aluno.av1 = float(data.get('av1'))
        aluno.av2 = float(data.get('av2'))
        aluno.media = (aluno.av1 + aluno.av2) / 2

        db.session.commit()

        jsonify({'message': 'Informações do aluno atualizadas com sucesso!'}), 200
        return redirect('/')


def calcular_idade(data_nascimento):
    data_atual = date.today()
    ano_nascimento, mes_nascimento, dia_nascimento = map(
        int, data_nascimento.split('-'))
    idade = data_atual.year - ano_nascimento
    if (data_atual.month, data_atual.day) < (mes_nascimento, dia_nascimento):
        idade -= 1
    return idade
