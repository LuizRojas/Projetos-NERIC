from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlachemy
from gerador import Gerador


app = Flask(__name__)

def gerar_senha(tamanho=12):
    gdr = Gerador()
    return gdr.gerar_senha(tamanho)

@app.route('/gerar_senha/<int:tamanho>', methods=['GET'])  # a rota aceita um parâmetro <int:tamanho> na URL.
def gerar_senha_api(tamanho):
    if (tamanho < 6):
        return jsonify({"erro": "A senha deve ter pelo menos 6 caracteres."}), 400  # o usuario ta enviando uma requisicao em um formato incorreto
    senha = gerar_senha(tamanho)
    return jsonify({"senha": senha})

if __name__ == '__main__':
    app.run(debug=True)