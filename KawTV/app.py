from flask import Flask, render_template, request,session, url_for, redirect, flash
import database

app = Flask (__name__)
app.secret_key = "chave_muito_segura"

@app.route ('/')
def index ():
    return render_template ('index.html')

@app.route ('/cadastro')
def cadastro ():
    return render_template ('cadastro.html')

if __name__ == '__main__':
    app.run (debug = True)