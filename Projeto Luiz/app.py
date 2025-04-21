from flask import Flask, render_template, request
from models import db, Lead

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leads.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    empreendimentos = [
        {
            'nome': 'Residencial Aurora',
            'descricao': '2 e 3 quartos com varanda gourmet.',
            'imagens': ['empreendimento0_1.jpg', 'empreendimento0_2.jpg', 'empreendimento0_3.jpg']
        },
        {
            'nome': 'Vitale Park',
            'descricao': 'Localização privilegiada e lazer completo.',
            'imagens': ['empreendimento1_1.jpg', 'empreendimento1_2.jpg', 'empreendimento1_3.jpg']
        },
        {
            'nome': 'Vista Bella',
            'descricao': 'Apartamentos com vista panorâmica.',
            'imagens': ['empreendimento2_1.jpg', 'empreendimento2_2.jpg', 'empreendimento2_3.jpg']
        },
    ]
    return render_template('index.html', empreendimentos=empreendimentos)

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    empreendimento = request.form['empreendimento']

    novo_lead = Lead(nome=nome, email=email, telefone=telefone, empreendimento=empreendimento)
    db.session.add(novo_lead)
    db.session.commit()

    return f"<h1>Obrigado pelo cadastro, {nome}!</h1>"

if __name__ == '__main__':
    print("Iniciando o Flask...")
    app.run(debug=True)
