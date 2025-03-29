from flask import Flask, jsonify
from gerador import Gerador


app = Flask(__name__)

def gerar_senha(tamanho=12):
    gdr = Gerador()
    return gdr.gerar_senha(tamanho)

@app.route('/gerar_senha', methods=['GET'])
def gerar_senha_api():
    senha = gerar_senha(12)
    return jsonify({"senha": senha})

if __name__ == '__main__':
    app.run(debug=True)