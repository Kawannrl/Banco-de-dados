import sqlite3

def conectar_banco ():
    conexao = sqlite3.connect ("filmes.db")
    return conexao

def criar_tabela ():
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ("""create table if not exists filmes (id integer primary key autoincrement, titulo text, diretor text, ano integer)""")
    conexao.commit ()
    return True

def adicionar_filme (titulo, diretor, ano):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ("""insert into filmes (titulo, diretor, ano) values (?, ?, ?)""", (titulo, diretor, ano))
    conexao.commit ()
    return True

def atualizar_filme (titulo, diretor, ano, id):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ("""update filmes set titulo = ?, diretor = ?, ano = ? where id = ?""", (titulo, diretor, ano, id))
    conexao.commit ()
    return True

def apagar_filme (id):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ("""delete from filmes where id = ?""", (id,))
    conexao.commit ()
    return True

def buscar_filme ():
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ("""select * from filmes where ano > 2010""")
    lista_de_filme = cursor.fetchall ()

    if (not lista_de_filme):
        print ('LOG: Não tem filmes com lançmentos antes dessa data!')
        return False
    else:
        filmes = cursor.fetchone ()
        print (lista_de_filme)
        return filmes
    