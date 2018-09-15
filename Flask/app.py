from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index ():
    return '<h1>Ola mundo!</h1>'

@app.route('/login')
def login():
    return jsonify({'mensage':'Minha primeira api rest', 'data':datetime.now().strftime('%d-%b-%Y %H:%M:%S')})

if __name__ == '__main__': # isso faz ele entender que q o __main__ dele\
    # só será qdo o app.py estiver sendo executado
    app.run(host='0.0.0.0', port=5000, debug=True)