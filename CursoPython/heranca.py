#herança simples
class A:
    pass
class B(A):
    pass

#herança multipla
class D:
    pass
class E:
    pass
class F(D,E):
    pass

#herança simples

class veiculo:
    def __init__(self, cor,placa,ano, aro):
        self.cor = cor
        self.placa = placa
        self.ano = ano
        self.aro = aro
    
    def ligar_motor(self):
        print("ligando motor")

    def __str__(self):
      return self.cor

class motocicleta(veiculo):
    pass
class carro(veiculo):
    pass


class Caminhao(veiculo):
    def __init__(self,cor,placa,ano, aro, carregado):

        super().__init__(cor,placa,ano,aro)
        self.carregado = carregado


    def verificar_carregamento(self):
        print(f"{'sim' if self.carregado else 'Nao'} estou carregado")

#moto = motocicleta("branca", 123, 2014, 16)
#print(moto)
#moto.ligar_motor()

car = carro('VERDE','ABC-89',2015, 16)
car.ligar_motor()

caminhao = Caminhao("azul", '123-FG', 2011, 24 , False)
caminhao.verificar_carregamento()
print(caminhao)
