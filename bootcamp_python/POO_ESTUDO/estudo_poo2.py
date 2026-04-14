# Herança Simples

class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("ligando motor")

    def optimusprime(self):
        print("OPTIMUS PRIME LIGANDO")  
 
    def __str__(self):
        return f"{self.__class__.__name__} : {', '.join([f"{chave}={valor}" for chave, valor in self.__dict__.items() ])}"
       

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não' } estou carregado")


carro = Carro("verde", "H34H3-H3H", 4)
carro.ligar_motor()

moto = Motocicleta("Preta", "H5AD03-32", 4)
moto.ligar_motor()

caminhao = Caminhao("vermelho e azul", "Optimus-Prime", 8, False)
caminhao.optimusprime()
caminhao.esta_carregado()
print(caminhao)
print(moto)
print(carro)