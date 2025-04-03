from flask import Flask, render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import database

app = Flask (__name__)
app.secret_key = "SENHA SECRETA"

@app.route ('/')
def hello ():
    return render_template ('index.html')

@app.route ('/login', methods = ["GET", "POST"])
def login ():
    if request.method == "POST":
        form = request.form
        
        if database.fazer_login (form) == True:
            session ['usuario'] = form ['email']
            return redirect (url_for ('lista'))
        else:
            return "Ocorreu um erro ao fazer login"
    else:
        return render_template ('login.html')

@app.route ('/cadastro', methods = ["GET", "POST"])
def cadastro ():
    if request.method == "POST":
        form = request.form
        
        if database.criar_usuario (form) == True:
            return render_template ('login.html')
        else:
            return "Ocorreu um erro ao cadastrar o usuário"
    else:
        return render_template ('cadastro.html')
    
@app.route ('/lista', methods = ["GET", "POST"])
def lista ():
    
    if request.method == "POST":
        form = request.form
        
        if database.adicionar_tarefa (form, session ['usuario']) == True:
            return render_template ('lista.html')
        else:
            return "Ocorreu um erro ao adicionar um item a lista"
    else:
        if 'usuario' not in session:
            return redirect (url_for ('login'))
        tarefas = database.buscar_tarefas (session ['usuario'])
        print (tarefas)
        return render_template ('lista.html', usuario = session ['usuario'], tarefas = tarefas)

if __name__ == '__main__':
    app.run (debug = True)