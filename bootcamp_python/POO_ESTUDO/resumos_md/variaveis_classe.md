# Variaveis de Classe e De instancia 

Atributos de Instancia -> diferentes para cada objeto (cada objeto tem uma cópia)

Atributos de Classe -> são compartilhados entre os objetos

# Métodos de classe e Métodos estáticos
Metodos de classe -> ligados a classe, eles tem acesso ao estado da classe, pois recebe um parametro que aponta para a classse

Métodos estáticos -> não recebe um primeiro argumento explicito -> metodo vinculado a classe e ñ pode acessar ou modificar o estado da classe

# Métodos de classe x Métodos estáticos 
Método de classse -> recebe um primeiro parametro que aponta para a classe, enquanto um método estático não

Método de Classe -> pode acessar ou modificar o estado da classe enquanto um método estático não pode acessa-lo ou modificar

# Quando utilizar método de classe ou estático
Metodo de classe -> métodos de fabrica
Métodos estáticos -> funções utilitárias 

# Interfaces 
Interfaces elas definam o que uma classe deve fazer e não como

Python utiliza classes abstratas para criar contratos

# Criadno classes com Modo ABC
ABC -> Abstract base class 
ABC funciona decorando métodos da classe base como abstratos e em seguida registrando classess concretas como implementaçõess da base abstrata