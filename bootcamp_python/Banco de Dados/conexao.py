import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH/ "meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


def criar_tabela(conexao, cursor):
    cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')
    conexao.commit()


def criar_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', data)
    conexao.commit()


def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute('UPDATE clientes SET nome=?, email=? WHERE id=?;', data)
    conexao.commit()

# atualizar_registro(conexao, cursor, "robsonbanana", "macaco.ldbrito@gmail.com", 1)


def deletar_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?", data)
    conexao.commit()

# deletar_registro(conexao, cursor, 4)    

def inserir_muitos(conexao, cursor, dados):
    cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?, ?)', dados)
    conexao.commit()

# dados = [
        # ("Gustavo", "gustavo.ldbrito@gmail.com"),
       #  ("sophia", "sophie.fernandes@gmail.com"),
         #("davi", "davi.ldbrito@gmail.com"),
         #("robson", "derreteman@gmail.com")
# ]    

# inserir_muitos(conexao, cursor, dados)

def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

# print(cliente)

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome ASC, id;")

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(dict(cliente))

cliente = recuperar_cliente(cursor, 1)
print(dict(cliente))
print(cliente["id"])
