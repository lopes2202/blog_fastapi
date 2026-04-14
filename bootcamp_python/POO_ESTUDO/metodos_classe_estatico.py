class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome 
        self.idade = idade
        
    @classmethod
    def criar_partir_data_nascimento(cls, ano, mes, dia , nome):
        idade = 2026 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade  >= 18

pessoa = Pessoa.criar_partir_data_nascimento(2005, 2, 22, "Gabriel")
print(pessoa.nome, pessoa.idade)

print(Pessoa.e_maior_idade(16))
print(Pessoa.e_maior_idade(25))

        