import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def conectar_banco ():
    conexao = sqlite3.connect ("tarefas.db")
    return conexao

def criar_tabelas ():
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ('''create table if not exists usuarios (email text primary key, nome text, senha text)''')
    cursor.execute ('''create table if not exists tarefas (id integer primary key, conteudo text, esta_concluida integer, email_usuario text, foreign key(email_usuario) references usuarios(email))''')
    conexao.commit ()

def criar_usuario (formulario):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ('''select count (email) from usuarios where email = ?''', (formulario ['email'],))
    conexao.commit ()

    quantidade_de_email = cursor.fetchone ()
    if (quantidade_de_email [0] > 0):
        print ("LOG: Já existe esse e-mail cadastrado no banco!")
        return False
    
    senha_criptografada = generate_password_hash (formulario ['senha'])
    cursor.execute ('''insert into usuarios (email, nome, senha) values (?, ?, ?)''', (formulario ['email'], formulario ['nome'], senha_criptografada))
    conexao.commit ()
    return True

def fazer_login (formulario):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ('''select count (email) from usuarios where email = ?''', (formulario ['email'],))
    conexao.commit ()

    quantidade_de_email = cursor.fetchone ()
    print (quantidade_de_email)
    if (quantidade_de_email [0] < 0):
        print ("LOG: Já existe esse e-mail cadastrado no banco!")
        return False
    
    else:
        cursor = conexao.cursor ()
        cursor.execute ('''select senha from usuarios where email = ?''', (formulario ['email'],))
        conexao.commit ()
        senha_criptografada = cursor.fetchone ()
        resultado_verificacao = check_password_hash (senha_criptografada [0], formulario ['senha'])
        return resultado_verificacao
    
def adicionar_tarefa (formulario, email_usuario):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    conteudo = (formulario ['tarefa'])
    cursor.execute ('''insert into tarefas (conteudo, esta_concluida, email_usuario) values (?, ?, ?)''', (conteudo, 0, email_usuario))
    conexao.commit ()
    return True

def buscar_tarefas (email):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ("select id, conteudo, esta_concluida from tarefas where email_usuario = ?", (email,))
    tarefas = cursor.fetchall ()
    return tarefas
    

if __name__ == "__main__":
    criar_tabelas ()