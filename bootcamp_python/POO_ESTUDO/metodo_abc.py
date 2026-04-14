from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando")

    def desligar(self):
        print("Desligando") 
    @property
    def marca(self):
        return "LG"       

class ArCpndicionado(ControleRemoto):
    def ligar(self):
        print("Ligando")

    def desligar(self):
        print("Desligando")  
    @property
    def marca(self):
        return "samsung"       

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)
arcondicionado = ArCpndicionado()
arcondicionado.ligar()
print(arcondicionado.marca)
