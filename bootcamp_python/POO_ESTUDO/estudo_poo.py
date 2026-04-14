class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor 
        self.modelo = modelo 
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("BIBIBI")

    def parar(self):
        print("parando")

    def correr(self):
        print("correndo") 

    # def __str__(self):
     #   return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"    

    def __str__(self):
        return f"{self.__class__.__name__} : {', '.join([f"{chave}={valor}" for chave, valor in self.__dict__.items() ])}"
    
bicicleta_1 = Bicicleta("Amarela", "Caloi", 2015, 2000)
bicicleta_1.buzinar()
bicicleta_1.correr()
bicicleta_1.parar()

print(bicicleta_1)
     

