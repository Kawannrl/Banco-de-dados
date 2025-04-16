import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def conectar_banco ():
    conexao = sqlite3.connect ("musicas.db")
    return conexao

def criar_tabelas ():
    pass

if __name__ == '__main__':
    criar_tabelas ()