from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')

def details():
    return jsonify({
        'time': datetime.datetime.now(),
        'hostname' : socket.gethostname(),
        'message' :  'Esta tudo indo bem humano!!!!!!!!'
    })



@app.route('/api/v1/healthz')

def health():
    return jsonify({
        'status': 'UP'
    }), 200


if __name__ == '__main__':
    # O parâmetro host='0.0.0.0' é a chave aqui
    app.run(host='0.0.0.0', port=5000)
