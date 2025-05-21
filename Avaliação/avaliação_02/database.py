import sqlite3

def conectar_banco ():
    conexao = sqlite3.connect ("biblioteca.db")
    return conexao

def criar_tabela ():
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ("""create table if not exists alunos (id integer primary key autoincrement, nome text, turno text, turma text)""")
    cursor.execute ("""create table if not exists livros (id integer primary key autoincrement, titulo text, ano integer, autor text)""")
    cursor.execute ("""create table if not exists emprestimo (id integer primary key autoincrement, livro text, aluno text, data_emprestimo integer, data_prevista integer, status text)""")
    conexao.commit ()
    return True

def registrar_aluno (nome, turno, turma):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ("""insert into alunos (nome, turno, turma) values (?, ?, ?)""", (nome, turno, turma))
    conexao.commit ()
    return True

def atualizar_aluno (nome, turno, turma, id):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ("""update alunos set nome = ?, turno = ?, turma = ? where id = ?""", (nome, turno, turma, id))
    conexao.commit ()
    return True

def apagar_aluno (id):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ("""delete from alunos where id = ?""", (id,))
    conexao.commit ()
    return True

def registrar_livro (titulo, ano, autor):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ("""insert into livros (titulo, ano, autor) values (?, ?, ?)""", (titulo, ano, autor))
    conexao.commit ()
    return True

def atualizar_livro (titulo, ano, autor, id):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ("""update livros set titulo = ?, ano = ?, autor = ? where id = ?""", (titulo, ano, autor, id))
    conexao.commit ()
    return True

def apagar_livro (id):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ("""delete from livros where id = ?""", (id,))
    conexao.commit ()
    return True

def registrar_emprestimo (livro, aluno, data_emprestimo, data_prevista, status):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ("""insert into emprestimo (livro, aluno, data_emprestimo, data_prevista, status) values (?, ?, ?, ?, ?)""", (livro, aluno, data_emprestimo, data_prevista, status))
    conexao.commit ()
    return True

def atualizar_emprestimo (status, id):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ("""update livros set status where id = ?""", (status, id))
    conexao.commit ()
    return True

def buscar_emprestimo (aluno):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ("""select * from emprestimo where aluno = ?""", (aluno,))
    emprestimos = cursor.fetchall ()
    print (emprestimos)
    return emprestimos

def livros_atrasados ():
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ("""select * from emprestimo where status = pendente""")
    emprestimos_atrasados = cursor.fetchall ()
    print (emprestimos_atrasados)
    return emprestimos_atrasados
