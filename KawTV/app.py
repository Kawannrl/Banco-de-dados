from flask import Flask, render_template, request,session, url_for, redirect, flash
import database

app = Flask(__name__)
app.secret_key = 'chave-secreta-do-ourico'

@app.route ('/')
def index ():
    return redirect (url_for ('login'))

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route ('/confirmar-cadastro', methods = ['GET', 'POST'])
def cadastrar ():
    if request.method == "POST":
        form = request.form
        
        if database.criar_usuario (form ['email'], form ['nome'], form ['senha']) == True:
            return render_template ('login.html')
        else:
            flash ('Ocorreu um erro ao fazer o cadastro!', 'error')
            return redirect (url_for('cadastrar'))

    return render_template ('cadastro.html')
    
@app.route ('/login', methods = ["GET", "POST"])
def login ():
    if request.method == "POST":
        form = request.form
        
        email = form ["email"]
        senha = form ["senha"]
        
        if database.fazer_login (email, senha) == True:
            session ['nome'] = email
            return redirect (url_for ('home'))
        else:
            flash ('Ocorreu um erro ao fazer login!', 'error')
            return redirect (url_for('login'))
    else:
        return render_template ('login.html')
    
@app.route ('/home')
def home ():
    if 'nome' not in session:
        return (url_for ('login'))
    
    filmes = database.buscar_filme (session ['nome'])
    return render_template ('home.html', nome = session ['nome'], filmes = filmes)

@app.route ('/filmes', methods = ["GET", "POST"])
def novo_filme ():
    if 'nome' not in session:
        return (url_for ('login'))
    
    if request.method == "POST":
        form = request.form
        titulo = form ['titulo']
        estilo = form ['estilo']
        ano = form ['ano']
        descricao = form ['descricao']
        imagem = form ['imagem']
        id_usuario = session ['nome']
        if database.adicionar_filme (id_usuario, titulo, estilo, ano, descricao, imagem) == True:
            flash ("Filme adicionado com sucesso", "success")
            return redirect (url_for ('home'))
    return render_template ('adicionar.html')

@app.route ('/editar_filme/<int:id>', methods = ['GET', "POST"])
def editar_filme (id):
    
    if (request.method == "GET"):
        filmes = database.buscar_filme_por_id (id)
        return (render_template ("editar.html", filmes = filmes, id = id))
    
    if (request.method == "POST"):
        form = request.form
        titulo = form ['titulo']
        estilo = form ['estilo']
        ano = form ['ano']
        descricao = form ['descricao']
        imagem = form ['imagem']
        database.editar_filme (titulo, estilo, ano, descricao, imagem, id)
        return redirect (url_for ('home'))

@app.route('/apagar_filme/<int:id>')
def apagar_filme (id):
    
    if database.apagar_filme (id) == True:
        return redirect (url_for ('home'))
    else:
        return "Algo deu errado"

@app.route('/logout')
def logout():
    
    session.pop('nome', None)
    flash('Você foi desconectado com sucesso!', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run (debug = True)