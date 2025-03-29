from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
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
    origem = db.Column(db.String(100), nullable=False)

# Criar o banco de dados
with app.app_context():
    db.create_all()

def gerar_senha(tamanho=12):
    gdr = Gerador()
    return gdr.gerar_senha(tamanho)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listar_senhas', methods=['GET'])
def listar_senhas():
    senhas = Senha.query.all()
    return jsonify([{"id": s.id, "senha": s.senha, "origem": s.origem} for s in senhas])

@app.route('/gerar_senha', methods=['POST'])
def gerar_senha_api():
    data = request.json
    tamanho = data.get('tamanho', 12)  # Default 12 caracteres
    origem = data.get('origem', 'Desconhecido')

    if tamanho < 6:
        return jsonify({"erro": "Tamanho mínimo da senha é 6 caracteres"}), 400

    senha = gerar_senha(tamanho)

    # Salva no banco de dados
    nova_senha = Senha(senha=senha, origem=origem)
    db.session.add(nova_senha)
    db.session.commit()

    return jsonify({"id": nova_senha.id, "senha": senha, "origem": origem})

if __name__ == '__main__':
    app.run(debug=True)