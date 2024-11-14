from flask import Flask, jsonify, request

app = Flask(__name__)

frutas = [
    {
        'id': 1,
        'nome': 'maça',
        'cor': 'vermelha',
        'quantidade': 10
    },
    {
        'id': 2,
        'nome': 'banana',
        'cor': 'amarela',
        'quantidade': 5
    },
    {
        'id': 3,
        'nome': 'uva',
        'cor': 'roxa',
        'quantidade': 8
    }
]

# Listar todos os itens
@app.route('/frutas', methods=['GET']) # Metódo para listar frutas
def mostrar_todas_frutas():
    return jsonify(frutas) # Retorna a lista como JSON

# Listar itens por ID
@app.route('/frutas/<int:id>', methods=['GET']) # Retorna a fruta pelo ID
def mostrar_frutas_id(id):
    for fruta in frutas:
        if fruta['id'] == id:
            return jsonify(fruta)
        
        # Adicionar itens
@app.route('/frutas', methods=['POST']) # Adiciona uma fruta à lista
def adicionar_frutas():
    nova_fruta = request.get_json()
    frutas.append(nova_fruta)

    return jsonify(nova_fruta)
