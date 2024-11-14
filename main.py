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
