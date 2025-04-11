from flask import Flask, render_template, request,session, url_for, redirect, flash
import database

app = Flask (__name__)
app.secret_key = "chave_muito_segura"

# Cria um dicionário e usuários e senha, SERÁ MIGRADO PARA O BANCO DE DADOS

@app.route ('/') #rota para a página inicial
def index ():
    return render_template ('index.html')

@app.route ('/home')
def home ():
    return render_template ('home.html')

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
            session ['nome'] = (email,)
            return redirect (url_for ('home'))
        else:
            return ("Ocorreu um erro ao  fazer login!")
    else:
        return render_template ('login.html')
    
@app ('/home', methods = ["GET", "POST"])
def nova_musica ():
    if request.method == "POST":
        pass

# parte principal do
if __name__ == '__main__':
    app.run (debug = True)