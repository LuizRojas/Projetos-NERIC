from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from gerador import Gerador


app = Flask(__name__)

# banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///senhas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo do banco de dados
class Senha(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    senha = db.Column(db.String(255), nullable=False)

# Criar o banco de dados
with app.app_context():
    db.create_all()

def gerar_senha(tamanho=12):
    gdr = Gerador()
    return gdr.gerar_senha(tamanho)

@app.route('/gerar_senha/<int:tamanho>', methods=['GET'])  # a rota aceita um parâmetro <int:tamanho> na URL.
def gerar_senha_api(tamanho):
    if (tamanho < 6):
        return jsonify({"erro": "A senha deve ter pelo menos 6 caracteres."}), 400  # o usuario ta enviando uma requisicao em um formato incorreto
    senha = gerar_senha(tamanho)

    # return jsonify({"senha": senha})
    nova_senha = Senha(senha=senha)
    db.session.add(nova_senha)
    db.session.commit()

    return jsonify({"id": nova_senha.id, "senha": senha})

@app.route('/listar_senhas', methods=['GET'])
def listar_senhas():
    senhas = Senha.query.all()
    return jsonify([{"id": s.id, "senha": s.senha} for s in senhas])

if __name__ == '__main__':
    app.run(debug=True)