# POO (Progamação orientada a objetos)
estrutura o código abstraindo problemas em objeto do mundo real

dois conceitos chaves do POO : classes e objetos

# Paradigmas de programação
a forma de como solucionar os problemas através  do código

# Alguns paradigmas
Imperativo ou procedural
Funcional
Orientado a eventos

# Classe
Definir as caracteristicas e comportamentos de um objeto

# Objetos
Possuem as caracteristicas e comportamentos que foram definidos na classe

# Construtor
Método construtor -> sempre executado qnd uma nova instancia da classe é criada

Declarar metódo construtor da classe, exemplo - __init__

# Destrutor
Metodo destrutor semore é executado qnd uma instancia (objeto) é destruida
Python tem um coletor de lixo que lida com o gerenciamento de memória automaticamente 
Declarar o método destrutor da classe, exemplo __del__

# Herança em POO
é a capacidade de uma classe filha derivar ou herdar as caracteristicas e comportamentos da classe pai (base)

# Benefícios da herança
reutilização de código
adiciona mais recursos a uma classe sem modifica-la
natureza transitiva, se a classe B herdar da classe A, todas as subclasses de b herdarão automaticamente da classe A

# Herança simples e herança multipla 
Herana simples -> filha herda apenas uma classe pai
class A:
    pass
class B(A):    
Herança multipla -> filha herda de várias classes pai
class A:
    pass
class B:
    pass
Class C(A, B):
    pass    

# Comando Super
pode colocar o super em qualquer lugar, eu decido a hora que invocar

vai herdar as caracteristicas e o comportamento e qlqr a momento o python permite que voce sobrescreva e troque o comportamento ou as caracteristicas