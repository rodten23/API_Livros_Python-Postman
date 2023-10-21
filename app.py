# Aula do Canal Dev Aprender | Jhonatan de Souza: https://youtu.be/FBLAV1SbJFk

# API é um lugar para disponibilizar recursos e/ou funcionalidades.

# 1. Objetivo: criar API que disponibiliza a consulta, criação, edição e exclusão de livros.

# 2. URL base: local para os qual estaremos fazendo nossas requisições e, neste treinamento, será localhost

# 3. Endpoints: endereços que deverão ser consultado e verbos (funcionalidades) que serão disponibilizados

    # - localhost/livros (GET) # consultar de forma geral
    # - localhost/livros (POST) # criar novos livros
    # - localhost/livros/id (GET) # consultar livro específico
    # - localhost/livros/id (PUT) # modificar um livro específico
    # - localhost/livros/id (DELET) # excluir um livro específico

# 4. Quais recursos: lista e dados de livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Dança Com Lobos',
        'autor': 'Michael Blake'
    },
    {
        'id': 2,
        'titulo': 'O Universo numa Casca de Noz',
        'autor': 'Stephen Hawking'
    },
    {
        'id': 3,
        'titulo': 'A Arte Cavalheiresca do Arqueiro Zen',
        'autor': 'Eugen Herrigel'
    },
    {
        'id': 4,
        'titulo': 'Tao Te Ching',
        'autor': 'Lao Tse'
    },
    {
        'id': 5,
        'titulo': 'A Profecia Celestina',
        'autor': 'James Redfield'
    },
    {
        'id': 6,
        'titulo': 'O Senhor do Anéis - A Sociedade do Anel',
        'autor': 'J. R. R. Tolkien'
    },
]

# Consultar todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar por ID na URL
@app.route('/livros/<int:id>', methods=['GET']) # type: ignore
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
# Consultar livro por ID recebido no body JSON
@app.route('/livros/consultar_livro_por_id_json', methods=['GET']) # type: ignore
def consultar_livro_por_id_json():
    dados = request.get_json()
    id = dados["id"]
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        #else:
        #    return print("Desculpe, não temos nenhum livro com este ID!/n Favor, consulte novamente informando um ID válido./n Obrigado")
        
# Editar livro por ID na URL
@app.route('/livros/<int:id>', methods=['PUT']) # type: ignore
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
# Editar livro por ID recebido no body JSON
@app.route('/livros/editar_livro_por_id_json', methods=['PUT']) # type: ignore
def editar_livro_por_id_json():
    livro_alterado = request.get_json()
    id = livro_alterado["id"]
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# #Criar livro
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

#Criar livro
# @app.route('/livros', methods=['POST']) # type: ignore
# def incluir_novo_livro():
#     novo_livro = request.get_json()
#     id = novo_livro["id"]
#     for livro in livros:
#         if livro.get('id') == id:
#             print("Desculpe, mas este ID já está sendo usado por outro livro!/n Tente novamente com outro ID.")
#             return jsonify("'message': 'Desculpe, mas este ID já está sendo usado por outro livro!/n Tente novamente com outro ID.'")
#         else:
#             livros.append(novo_livro)
#             return jsonify(livros)

#Excluir livro por ID na URL
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

#Excluir livro por ID recebido no body JSON
@app.route('/livros/excluir_livro_por_id_json', methods=['DELETE'])
def excluir_livro_por_id_json():
    livro_excluido = request.get_json()
    id = livro_excluido["id"]
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

app.run(port=3000, host='localhost', debug=True)
