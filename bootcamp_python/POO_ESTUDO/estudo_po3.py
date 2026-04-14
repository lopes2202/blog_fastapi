class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__} : {', '.join([f"{chave}={valor}" for chave, valor in self.__dict__.items() ])}"
          
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self,cor_bico, **kw):
        super().__init__(**kw)
        self.bico = cor_bico

    
class Cachorro(Mamifero):
    pass

class FalarMixin:
    def falar(self):
        return "salve gostoso"

class Perry(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_pelo, cor_bico, nro_patas):
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)

perry = Perry(nro_patas=4, cor_pelo="Azul", cor_bico="laranja")
print(perry)

cachorro = Cachorro(nro_patas=4, cor_pelo="preto")
print(cachorro)
print(perry.falar())

   
    
