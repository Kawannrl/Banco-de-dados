import database
from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'chave_secreta_muito_segura' 

# Definindo a rota principal do site 
@app.route('/')
def index ():
    return render_template('index.html')

@app.route('/planejamento')
def planejamento ():
    return render_template('planejamento.html')

# Rota da página de cadastro
@app.route('/cadastro')
def cadastro ():
    return render_template('cadastro.html')

# Confirmação do cadastro
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    usuario = request.form['usuario']
    email = request.form['email']
    senha = request.form['senha']

    if database.criar_usuario(email, usuario, senha):
        return "Usuário criado com sucesso"
    else:
        return "Isso não funcionou"
    

# Rota para página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        conexao = database.conectar_banco()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        usuario = cursor.fetchone()
        conexao.close()

        if usuario and usuario[2] == senha:  # Verifica se a senha está correta
            session['usuario'] = usuario[0]  # Armazena o email do usuário na sessão
            return redirect(url_for('home'))
        else:
            flash("Usuário ou senha incorretos!", "danger")
    return render_template('login.html')


# Ver usuarios
@app.route('/usuarios')
def listar_usuarios():
    conexao = database.conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conexao.close()

    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/home')
def home():

    if 'usuario' not in session:
        return redirect(url_for('login'))
    
    viagens = database.buscar_viagens(session['usuario'])  # Busca as viagens do usuário
    return render_template('home.html', usuario=session['usuario'], viagens=viagens)


@app.route('/logout')
def logout():
    session.pop('usuario', None)  # Remove o usuário da sessão
    return redirect(url_for('login'))

@app.route('/nova', methods=['GET', 'POST'])
def nova_viagem():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    

    if request.method == 'POST':
        destino = request.form['destino']
        data_prevista = request.form['data_prevista']
        status = request.form['status']
        imagem = request.form['imagem']
        gastos = request.form['gastos']
        dinheiro_guardado = request.form['dinheiro_guardado']
        id_usuario = session['usuario']  # Usa o email do usuário logado
        database.criar_projeto(id_usuario, destino, data_prevista, status, imagem, gastos, dinheiro_guardado)
        flash("Viagem criada com sucesso!", "success")
        return redirect(url_for('home'))
    return render_template('nova_viagem.html')

@app.route('/excluir-viagem', methods=['POST'])
def excluir_viagem ():
    viagem_id = request.form.get ('viagem_id')
    database.apagar_viagens (viagem_id)
    return redirect (url_for ('home'))

@app.route('/excluir-usuario', methods=['POST'])
def excluir_usuario ():
    usuario_id = request.form.get ('usuario_id')
    database.apagar_usuario (usuario_id)
    return redirect (('/usuarios'))
    

if __name__ == '__main__':
    app.run(debug=True) 