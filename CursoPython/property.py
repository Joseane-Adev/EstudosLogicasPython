#property
class  Foo:
    def __init__(self, x=None):
            self._x = x
            #a variavel privada _x recebe o valor de x, que inicialmente é none
    
    #para retornar valor de uma variavel privada
    @property
    def x(self):
       
       return self._x or 0
    #retorna o valor da variavel privada ou 0

    #pra fazer uma alteração na propriedade é precisso setar
    @x.setter
    def x(self, valor):
        self._x += valor

    #para deletar
    @x.deleter
    def x(self):
         self._x = 0

foo = Foo(30)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)
