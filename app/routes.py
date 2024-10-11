from app import app
from flask import render_template, request
import requests
import json
link = 'https://flasktintcarolina-default-rtdb.firebaseio.com/'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',titulo="Página Inicial")

@app.route('/contato')
def contato():
    return render_template('contato.html', titulo="Contatos")

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo="Cadastrar")

@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    try:
        cpf        = request.form.get("cpf")
        nome       = request.form.get("nome")
        telefone   = request.form.get("telefone")
        endereco   = request.form.get("endereco")
        dados      = {"cpf":cpf, "nome": nome, "telefone":telefone, "endereco":endereco}
        requisicao = requests.post(f'{link}/cadastrar/.json', data = json.dumps(dados))
        return 'Cadastrado com sucesso!'
    except Exception as e:
        return f'Ocorreu um erro\n +{e}'

@app.route('/listar')
def listarTudo():
    try:
        requisicao = requests.get(f'{link}/cadastrar/.json') #solicita o dado
        dicionario = requisicao.json()
        return dicionario
    except Exception as e:
        return f'Algo deu errado \n {e}'

@app.route('/listarIndividual')
def listarLindividual():
    try:
        requisicao = request.get(f'{link}/cadastrar.json') #solicitando o
        dicionario = requisicao.json()
        idCadastro = "" #coletar o id
        for codigo in dicionario:
            chave = dicionario[codigo]['cpf']
            if chave == '212':
                idCadastro = codigo
                return idCadastro
    except Exception as e:
        return f'Algo deu errado \n {e}'

@app.route('/atualizar')
def atualizar():
    try:
        dados = {"nome":"joão"}
        requisicao = requests.patch(f'{link}/cadastrar/-O8mk9wgyymPZE2qtWH6/.json', data=json.dumps(dados))
        return "Atualizado com sucesso!"
    except Exception as e:
        return f'Algo deu errado \n {e}'

@app.route('/excluir')
def excluir():
    try:
        requisicao = requests.delete(f'{link}/cadastrar/-O8mk9wgyymPZE2qtWH6/.json')
        return "Excluído com sucesso!"
    except Exception as e:
        return f'Algo deu errado \n {e}'

