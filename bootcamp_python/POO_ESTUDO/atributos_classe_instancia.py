class Estudante:
    escola = "Gran" # varaiveis de classe unica para todos objetos

    def __init__(self, nome, matricula):
        self.nome = nome # variveis de instancia unica por objeto, cada objeto tem uma copia das variaveis
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola} "  
    

estudante = Estudante("Gabriel", 2314290121) 
print(estudante)   
estudante_2 = Estudante("Sophia", 30323233)
estudante_2.escola = "IESB"
print(estudante_2)




