from abc import ABC, abstractmethod

class Conta:
    def __init__(self, saldo, numero, agencia, cliente):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()

    @property
    def historico(self):
        return self._historico


    def saldo(self):
        pass

    @classmethod    
    def nova_conta(cls, cliente, numero, limite=500, limite_saques=3):
        return cls(0, numero, "0001", cliente, limite, limite_saques)
    
    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            print("Saldo realizado com sucesso")
            return True
        else:
            print("Saldo insuficiente")
            return False

    
    def depositar(self, valor):
        self._saldo += valor 
        return True
    
class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente,  limite, limite_saques):
        self._limite = limite
        self._limitesaque = limite_saques
        super().__init__(saldo, numero, agencia, cliente)

class Historico():
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao) 


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_operacao = conta.depositar(self.valor)
        if sucesso_operacao:
            conta.historico.adicionar_transacao(self)
        else: 
            print("Operação sem sucesso")    

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        saque_sucedido = conta.sacar(self.valor)
        if saque_sucedido:
            conta.historico.adicionar_transacao(self)
        else:
            print("Operação sem sucesso")

class Cliente:
    def __init__(self, endereco, contas= None):
        self._endereco = endereco
        self._contas = contas or []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)   

    def adicionar_conta(self, conta):
        self._contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        self.nome = nome
        self._cpf = cpf
        self.data_nascimento = data_nascimento
        super().__init__(endereco)


clientes = []
contas = []

def filtrar_dados(cpf, clientes):
        clientes_filtrados = [cliente for cliente in clientes if cliente._cpf == cpf]
        return clientes_filtrados[0] if clientes_filtrados else None

def exibir_extrato(clientes):
        cpf = input("Informe o seu CPF:  ")
        cliente = filtrar_dados(cpf, clientes)
        if not cliente:
            print("Cliente não encontrado")
            return
        else:
            conta = cliente._contas[0]

        transacoes = conta.historico._transacoes
        for transacao in transacoes:
            valor_da_operacao = transacao.valor

            nome_da_operacao = transacao.__class__.__name__

            print(f"{nome_da_operacao}: R$ {valor_da_operacao:2f}")

def sacar_novo(clientes):
    cpf = input("Informe o seu CPF: ")
    cliente = filtrar_dados(cpf, clientes)
    if not cliente:
        print("Cliente não encontrado")
        return
    else: 
        conta = cliente._contas[0]
        valor_saque = float(input("Qual seria o valor do saque? "))
        transacao = Saque(valor_saque)

        cliente.realizar_transacao(conta, transacao)  


def criar_cliente(clientes):
        cpf = input("Informe seu CPF: ")
        cliente = filtrar_dados(cpf, clientes)
        if cliente:
            print("Já existe um cliente com esse CPF")
            return
            
        nome = input("Informe seu Nome: ")
        data = input("Informe a Data: ")
        endereco = input("Informe seu Endereço: ")
        novo_cliente = PessoaFisica(nome=nome, data_nascimento=data, endereco=endereco, cpf=cpf)
        clientes.append(novo_cliente)
        print("Cliente cadastrado foi com sucesso")

def criar_conta(clientes):
        cpf = input("Informe seu CPF")
        cliente = filtrar_dados(cpf, clientes)
        numero = len(contas) + 1
        if not cliente:
            print("Não foi possivel criar a conta! ")
            return    
        else:
            nova_conta = ContaCorrente(0, numero, "0001", cliente, 500, 3)
            contas.append(nova_conta)
            cliente.adicionar_conta(nova_conta)                  


menu = """
[nu] Cadastrar Cliente
[nc] Cadastrar Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

while True:

    opcao = input(menu)

    if opcao == "nu":
        criar_cliente(clientes)

    elif opcao == "nc":
        numero_conta = len(contas) + 1
        criar_conta(clientes)    

    elif opcao == "d":
        cpf = input("Informe o seu CPF:  ")
        cliente = filtrar_dados(cpf, clientes)
        if not cliente:
            print("Cliente não encontrado")
        else:
            valor = float(input("Informe o valor do Depósito: "))
            transacao = Deposito(valor)
            if cliente._contas:
                conta = cliente._contas[0]
                cliente.realizar_transacao(conta, transacao) 
            else:
                print("Operação invalida, tente novamente!")

    elif opcao == "s":
        sacar_novo(clientes)

    elif opcao == "e":
        exibir_extrato(clientes)        
    elif opcao == "q":
        break

    else:
        print("Operação invalida.")   



    

        
        


