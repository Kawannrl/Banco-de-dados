import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def conectar_banco ():
    conexao = sqlite3.connect ("musicas.db")
    return conexao

def criar_tabelas ():
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ('''create table if not exists usuarios (email text primary key, nome text, senha text)''')
    cursor.execute ('''create table if not exists musicas (id integer primary key, id_usuario text, musica_nome text, artista text, status integer, imagem text, letra text)''')
    conexao.commit ()
    
def criar_usuario (email, nome , senha):
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
        verificar_senha = check_password_hash (senha_criptografada [0], senha)
        return verificar_senha
    
def buscar_musica (id_usuario):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ('''select musica_nome, artista, status, imagem, letra from musicas where id_usuario = ?''', (id_usuario,))
    musicas = cursor.fetchall ()
    return musicas
    
def criar_musica (id_usuario, musica_nome, artista, status, imagem, letra):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ('''insert into musicas (id_usuario, musica_nome, artista, status, imagem, letra) values (?, ?, ?, ?, ?, ?)''', (id_usuario, musica_nome, artista, status, imagem, letra))
    conexao.commit ()
    return True
    
def apagar_usuario (email):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ('''delete from usuarios where email = ?''', (email,))
    cursor.execute ('''delete from musicas where email = ?''', (email,))
    conexao.commit ()
        

# PARTE PRINCIPAL DO PROGRAMA
if __name__ == '__main__':
    criar_tabelas ()