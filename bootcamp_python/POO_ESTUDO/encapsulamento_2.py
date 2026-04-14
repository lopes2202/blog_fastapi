# Propriedades

class Foo:
    def __init__(self, x=None):
        self._x = x

    @property # retornar valor
    def x(self):
        return self._x or 0

    @x.setter # alterar valor ou fazer uma definição
    def x(self, value): 
        self._x += value

    @x.deleter
    def x(self): 
        self._x = -1
 
foo = Foo(10)
print(foo.x)
foo.x = 10
del foo.x
print(foo.x)