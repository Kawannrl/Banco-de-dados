import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def conectar_banco ():
    conexao = sqlite3.connect ("Ourico_TV.db")
    return conexao

def criar_tabelas ():
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ('''create table if not exists usuarios (email text primary key, nome text, senha text)''')
    cursor.execute ('''create table if not exists filmes (id integer primary key, id_usuario text, titulo text, estilo text, ano text, descricao text, imagem text)''')
    conexao.commit ()
    conexao.close ()
    
def criar_usuario (email, nome, senha):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ('''select count (email) from usuarios where email = ?''', (email,))
    conexao.commit ()
    quantidade_de_email = cursor.fetchone ()
    
    if (quantidade_de_email [0] > 0):
        print ("LOG: Já existe esse e-mail cadastrado no banco!")
        return False
    
    senha_criptografada = generate_password_hash (senha)
    cursor.execute ('''insert into usuarios (email, nome, senha) values (?, ?, ?)''', (email, nome, senha_criptografada))
    conexao.commit ()
    return True

def fazer_login (email, senha):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ('''select count (email) from usuarios where email = ?''', (email,))
    quantidade_de_email = cursor.fetchone ()
    
    if (quantidade_de_email [0] < 0):
        print ("LOG: Já existe esse email cadastrado no banco de dados!")
        return False
    else:
        cursor.execute ('''select senha from usuarios where email = ?''', (email,))
        senha_criptografada = cursor.fetchone ()
        print (senha_criptografada)
        print (senha)
        verificar_senha = check_password_hash (senha_criptografada [0], senha)
        return verificar_senha
    
def adicionar_filme (usuario_id, titulo, estilo, ano, descricao, imagem):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ('''insert into filmes (usuario_id = ?, titulo = ?, estilo = ?, ano = ?, descricao = ?, imagem = ?) values (?, ?, ?, ?, ?, ?)''', (usuario_id, titulo, estilo, ano, descricao, imagem))
    conexao.commit 
    return True

def buscar_filme (id_usuario):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ('''select titulo, estilo, ano, descricao, imagem from filmes where id_usuario = ?''', (id_usuario,))
    filmes = cursor.fetchall ()
    return filmes

if __name__ == '__main__':
    criar_tabelas ()