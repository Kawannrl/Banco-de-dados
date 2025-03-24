import sqlite3

def conectar_banco ():
    conexao = sqlite3.connect ("trvl.db")
    return conexao 

def criar_tabelas ():
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ('''create table if not exists usuarios
                   (email text primary key,nome text,senha text)''')
    
    cursor.execute ('''create table if not exists projetos_de_viagem
                   (id integer primary key,id_usuario text,destino text,data_prevista text,
                   status text,imagem text,gastos real,dinheiro_guardado real)''')
    
    conexao.commit ()

def adicionar_usuario_viagem (email, id_projeto):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    
    try:
        cursor.execute ('''INSERT INTO usuarios_projetos (email_usuario, id projeto) values (?, ?)''', (email, id_projeto))
        conexao.commit ()
        return True
    except sqlite3.IntegrityError:
        return False
    
    finally:
        conexao.close ()


def criar_usuario (email, nome, senha):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    
    try:
        # PREENCHA AQUI - QUAL O COMANDO CRIAR UM NOVO USUÁRIO
        cursor.execute ('insert into usuarios (email, nome, senha) VALUES (?, ?, ?)', (email, nome, senha))
        conexao.commit ()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close ()

def criar_projeto (id_usuario,destino,data_prevista,status,imagem,gastos,dinheiro_guardado):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    
    try:
        cursor.execute ('''INSERT INTO projetos_de_viagem(id_usuario,destino,data_prevista,
                       status,imagem,gastos,dinheiro_guardado) values (?, ?, ? , ?, ?, ?, ?)'''
                       ,(id_usuario,destino,data_prevista,status,imagem,gastos,dinheiro_guardado))
        conexao.commit ()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close ()  

def buscar_viagens (id_usuario):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    # PREENCHA AQUI, BUSCAR TODAS AS VIAGENS ordem: destino, data prevista, status, imagem
    cursor.execute ("SELECT destino, data_prevista, status, imagem, id FROM projetos_de_viagem WHERE id_usuario = ?", (id_usuario,))
    viagens = cursor.fetchall ()
    conexao.close ()

    return viagens


def apagar_viagens (id_viagem):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    
    try:
        # PREENCHA AQUI - QUAL O COMANDO CRIAR UM NOVO USUÁRIO
        cursor.execute ('DELETE FROM projetos_de_viagem WHERE id = ?', (id_viagem,))
        conexao.commit ()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close ()

def mostrar_id_viagens (id_email):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    
    try:
        # PREENCHA AQUI - QUAL O COMANDO CRIAR UM NOVO USUÁRIO
        cursor.execute ('SELECT * FROM projetos_de_viagem WHERE id_usuario = ?', (id_email,))
        conexao.commit ()
        viagens = cursor.fetchall ()
        return viagens
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close ()
        
def apagar_usuario (email):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    
    try:
        # PREENCHA AQUI - QUAL O COMANDO CRIAR UM NOVO USUÁRIO
        cursor.execute ('DELETE FROM usuarios WHERE email = ?', (email,))
        cursor.execute ('DELETE FROM projetos_de_viagem WHERE id_usuario = ?', (email,))
        conexao.commit ()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close ()

def mudar_nome (nome, email):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    
    try:
        # PREENCHA AQUI - QUAL O COMANDO CRIAR UM NOVO USUÁRIO
        cursor.execute ('UPDATE usuarios SET nome = ? WHERE email = ?', (nome,email,))
        conexao.commit ()
        viagens = cursor.fetchall ()
        return viagens
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close ()


def mudar_senha (senha, email):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    
    try:
        # PREENCHA AQUI - QUAL O COMANDO CRIAR UM NOVO USUÁRIO
        cursor.execute ('UPDATE usuarios SET senha = ? WHERE email = ?', (senha,email,))
        conexao.commit ()
        viagens = cursor.fetchall ()
        return viagens
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close ()
        
        
def editar_viagem (destino,data_prevista,status,imagem,gastos,dinheiro_guardado, id_usuario):
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    
    try:
        # PREENCHA AQUI - QUAL O COMANDO CRIAR UM NOVO USUÁRIO
        cursor.execute ('UPDATE projetos_de_viagem SET destino = ?, data_prevista = ?, status = ?, imagem = ?, gastos = ?, dinheiro_guardado = ? WHERE id_usuario = ?', (destino, data_prevista, status, imagem, gastos, dinheiro_guardado, id_usuario,))
        conexao.commit ()
        viagens = cursor.fetchall ()
        return viagens
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close ()

if __name__ == '__main__': 
    conexao = conectar_banco ()
    criar_tabelas ()
    id_viagens = mostrar_id_viagens ("kawann.rl08@gmail.com")
    print (id_viagens)
    #apagar_viagens ("1")
    # #apagar_usuario ("kawann.rl08@gmail.com")
    # mudar_nome ("Kawann", "kawann.rl08@gmail.com")
    mudar_senha ("321", "kawann.rl08@gmail.com")
    editar_viagem ("Espanha", "27/12/2025", "Em andamento", "", "10.000", "500", "kawann.rl08@gmail.com")