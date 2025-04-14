from flask import Flask, render_template, request,session, url_for, redirect, flash
import database

app = Flask (__name__)
app.secret_key = "chave_muito_segura"

# Cria um dicionário e usuários e senha, SERÁ MIGRADO PARA O BANCO DE DADOS

@app.route ('/') #rota para a página inicial
def index ():
    return render_template ('index.html')

@app.route ('/cadastro') #rota para a página de login
def cadastro ():
    return render_template ('cadastro.html')

@app.route ('/cadastrar', methods = ["POST"])
def cadastrar ():
    if request.method == "POST":
        form = request.form
        
        email = form ["email"]
        nome = form ["nome"]
        senha = form ["senha"]
        
        if database.criar_usuario (email, nome, senha) == True:
            return render_template ('login.html')
        else:
            return ("Ocorreu um erro ao cadastrar o usuário!")
    else:
        return render_template ('cadastro.html')
    
@app.route ('/login', methods = ["GET", "POST"]) #rota para a página de login
def login ():
    if request.method == "POST":
        form = request.form
        
        email = form ["email"]
        senha = form ["senha"]
        
        if database.fazer_login (email, senha) == True:
            session ['nome'] = (email)
            return redirect (url_for ('home'))
        else:
            return ("Ocorreu um erro ao  fazer login!")
    else:
        return render_template ('login.html')
    
@app.route ('/home')
def home ():
    if 'nome' not in session:
        return (url_for ('login'))
    
    musicas = database.buscar_musica (session ['nome'])
    return render_template ('home.html', nome = session ['nome'], musicas = musicas)

@app.route ('/novo', methods = ["GET", "POST"])
def nova_musica ():
    if 'nome' not in session:
        return (url_for ('login'))
    
    if request.method == "POST":
        form = request.form
        musica_nome = form ['musica_nome']
        artista = form ['artista']
        status = form ['status']
        imagem = form ['imagem']
        letra = form ['letra']
        id_usuario = session ['nome']
        database.criar_musica (id_usuario, musica_nome, artista, status, imagem, letra)
        flash ("Música criada com sucesso", "success")
        return redirect (url_for ('home'))
    return render_template ('nova_musica.html')
    
# parte principal do
if __name__ == '__main__':
    app.run (debug = True)