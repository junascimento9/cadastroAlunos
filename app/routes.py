# app/routes.py 
from flask import render_template, request, redirect, flash
from app import app 
from app.models import Aluno
from datetime import date

alunos = []
next_id = 1

@app.route('/') 
def index():     
    return render_template('index.html', alunos=alunos) 

@app.route('/add', methods=['POST']) 
def add():     
     global next_id     
     cpf = request.form['cpf']     
     nome = request.form['nome']     
     data_nascimento = request.form['data_nascimento']     
     sexo = request.form['sexo']     
     av1 = float(request.form['av1'])     
     av2 = float(request.form['av2'])     
     media = (av1 + av2) / 2     
     idade = calcular_idade(data_nascimento)  

     aluno = Aluno(next_id, cpf, nome, data_nascimento, sexo, idade, av1, av2, media)     
     alunos.append(aluno)     
     next_id += 1    

     flash('Aluno cadastrado com sucesso!', 'success')     
     return redirect('/') 

@app.route('/delete', methods=['POST']) 
def delete(id):     
    aluno = find_aluno_by_id(id)     
    if aluno:         
        alunos.remove(aluno)         
        flash('Aluno removido com sucesso!', 'success')     
    else:         
        flash('Aluno não encontrado!', 'error')     
    return redirect('/')

@app.route('/edit/<int:id>', methods=['GET', 'POST']) 
def edit(id):     
    aluno = find_aluno_by_id(id)     
    if not aluno:         
        flash('Aluno não encontrado!', 'error')         
        return redirect('/')
         
    if request.method == 'POST':         
        aluno.cpf = request.form['cpf']         
        aluno.nome = request.form['nome']         
        aluno.data_nascimento = request.form['data_nascimento']        
        aluno.sexo = request.form['sexo']         
        aluno.av1 = float(request.form['av1'])         
        aluno.av2 = float(request.form['av2'])         
        aluno.media = (aluno.av1 + aluno.av2) / 2         
        aluno.idade = calcular_idade(aluno.data_nascimento)         
        flash('Informações do aluno atualizadas com sucesso!', 'success')         
        return redirect('/') 
        
    return render_template('edit.html', aluno=aluno) 

def find_aluno_by_id(id):     
    for aluno in alunos:         
        if aluno.id == id:             
            return aluno

def calcular_idade(data_nascimento):     
    data_atual = date.today()     
    ano_nascimento, mes_nascimento, dia_nascimento = map(int, data_nascimento.split('-'))     
    idade = data_atual.year - ano_nascimento     
    if (data_atual.month, data_atual.day) < (mes_nascimento, dia_nascimento):         
        idade -= 1     
    return idade