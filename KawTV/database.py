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
    
def criar_usuario (formulario):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ('''select count (email) from usuarios where email = ?''', (formulario['email'],))
    conexao.commit ()
    quantidade_de_email = cursor.fetchone ()
    
    if (quantidade_de_email [0] > 0):
        print ("LOG: Já existe esse e-mail cadastrado no banco!")
        return False
    
    senha_criptografada = generate_password_hash (formulario['senha'])
    cursor.execute ('''insert into usuarios (email, nome, senha) values (?, ?, ?)''', (formulario['email'], formulario['nome'], senha_criptografada))
    conexao.commit ()
    return True

def fazer_login (formulario):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ('''select count (email) from usuarios where email = ?''', (formulario['email'],))
    quantidade_de_email = cursor.fetchone ()
    
    if (quantidade_de_email [0] < 0):
        print ("LOG: Já existe esse email cadastrado no banco de dados!")
        return False
    else:
        cursor.execute ('''select senha from usuarios where email = ?''', (formulario['email'],))
        senha_criptografada = cursor.fetchone ()
        verificar_senha = check_password_hash (senha_criptografada [0], formulario['senha'])
        return verificar_senha
    
def adicionar_filme (usuario_id, titulo, estilo, ano, descricao, imagem):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ('''insert into filmes (usuario_id = ?, titulo = ?, estilo = ?, ano = ?, descricao = ?, imagem = ?) values (?, ?, ?, ?, ?, ?)''', (usuario_id, titulo, estilo, ano, descricao, imagem))
    conexao.commit 
    return True

if __name__ == '__main__':
    criar_tabelas ()