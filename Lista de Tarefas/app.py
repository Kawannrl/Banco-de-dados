from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
import database

app = Flask (__name__)

@app.route ('/')
def hello ():
    return render_template ('index.html')

@app.route ('/login')
def login ():
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

if __name__ == '__main__':
    app.run (debug = True)