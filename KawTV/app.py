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
        
        if database.criar_usuario (form) == True:
            return render_template ('login.html')
        else:
            return ("Ocorreu um erro ao cadastrar o usuário!")

    return render_template ('cadastro.html')
    
@app.route ('/login', methods = ["GET", "POST"])
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
    
if __name__ == '__main__':
    app.run (debug = True)