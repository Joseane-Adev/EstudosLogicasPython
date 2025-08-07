

class Bicicleta:
    #caracteristicas da classe
    #self é uma referencia para o objeto, quer dizer que é a instancia do objeto
    #metodo construtor def_init_()
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

#metodos para definir comportamentos
    def buzinal(self):
        print("Bi,BI")
    
    def parar(self):
        print("Stop")
    
    def correr(self):
        print("pedalando")

    #não funcionou
    #def __str__(self):
        #return f"Bicicleta: {self.cor}, {self.modelo}"
    
    #representar a classe
    def __str__(self):
       return f"{self.__class__.__name__}: {self.cor}, {self.modelo}"



#instancia de Bicicleta
b1 = Bicicleta("vermelha", "caloi", 2022, 800)
print(b1)
b1.buzinal()
b1.parar()
b1.correr()
#acessar
print(b1.ano)

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)
#acessar
print(b2.cor)
print(b2.ano)
Bicicleta.correr(b2)
b2.parar()

# construtores e destrutores
# 
class Cachorro:

    def __init__(self, nome, cor, acordado=False):
         print("inicializando a classe....")
         self.nome = nome
         self.cor = cor
         self.acordado =acordado
    
    def latir(self):
        print("AU,AU")

    
    def __del__(self):
        print("destruindo instancia")



c= Cachorro("pitbul", "branco")
c.latir()
del c






