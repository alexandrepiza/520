from flask import Flask, jsonify
from datetime import datetime
from pymongo import MongoClient
from bson import ObjectId
from json import loads, dumps
import psycopg2

app = Flask(__name__)
# Conexao com mongodb
client = MongoClient()
db = client['projeto']

# Conexao com postgresql
con = psycopg2.connect(
    'host=127.0.0.1 dbname=projeto user=admin password=4linux')
cur = con.cursor()


@app.route('/postgresql')
def postgres():
    cur.execute("select * from scripts;")
    date = cur.fetchall()
    lista = []
    for x in date:
        aux = {"_id": x[0], "nome": x[1], "idade": x[2]}
        lista.append(aux)

    return jsonify(lista)


@app.route('/mongo')
def mongo():
    lista = []
    for x in db.usuarios.find():
        lista.append(x)
    return jsonify(dumps(lista))


def serial(dct):
    for k in dct:
        if isinstance(dct[k], ObjectId):
            dct[k] = 'objectid' 
    return dct
@app.route('/mongo2')
def mongo2():
    return jsonify(([serial(x) for x in db.usuarios.find()]))

def serial(dct):
    for k in dct:
        if isinstance(dct[k], ObjectId):
            dct[k] = 'objectid' 
    return dct
@app.route('/teste/<variavel_busca>')
def teste(variavel_busca):
    return jsonify(([serial(x) for x in db.usuarios.find({"nome":variavel_busca})]))


@app.route('/login')
def login():
    return jsonify({'mensagem': 'Minha primeira api rest',
                    'data': datetime.now().strftime(
                        '%d-%b-%Y %H:%M:%S')})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)