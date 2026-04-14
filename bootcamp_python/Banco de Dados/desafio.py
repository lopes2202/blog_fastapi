import sqlite3 
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH/ "clientes.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


def criar_tabela(conexao, cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientela (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome VARCHAR(100), 
            documento VARCHAR(20), 
            tipo VARCHAR(10), 
            endereco VARCHAR(150)
        )
    """)
    conexao.commit()

def inserir_cliente(conexao, cursor):
    nome = input("Informe seu Nome: ")
    tipo = input("É Pessoa Fisica(PF) ou Pessoa Juridica(PJ)? ").upper().strip()
    endereco = input("Informe o endereço: ")
    
    if tipo == "PF":
        documento = input("Informe seu CPF ")
    elif tipo == "PJ":
        documento = input("Informe seu CNPJ ") 
    else:      
        print("Tipo de cliente inválido!")  
        return
    dados = (nome, documento, tipo, endereco)
    cursor.execute("INSERT INTO clientela (nome, documento, tipo, endereco) VALUES (?, ? , ?, ?)", dados) 
    conexao.commit()
    print("Cadastrado com sucesso!")


def listar_cliente(cursor):
    cursor.execute("SELECT * FROM clientela")
    lista_clientes = cursor.fetchall()
    if not lista_clientes:
        print("Lista vazia de Clientes")
        return
    print(f"\n{'TIPO':<15} | {'NOME':<20} | DOCUMENTO")
    print("-" * 60)

    for cliente in lista_clientes:
            if cliente["tipo"] == "PF":
                categoria = "PESSOA FISICA"
            else: 
                categoria = "PESSOA JURIDICA" 

            print(f"{categoria:<15} | {cliente['nome']:<20} | DOC: {cliente['documento']}")        

criar_tabela(conexao, cursor)

menu = """
[1] Cadastrar 
[2] Listar
[0] Sair

"""


while True:
    opcao = input(menu)

    if opcao == "1":
        inserir_cliente(conexao, cursor)
    elif opcao == "2":
        listar_cliente(cursor)
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção invalida")

conexao.close()                

     
