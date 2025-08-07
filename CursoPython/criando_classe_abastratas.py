#fazer classe abstrata 

from abc import ABC, abstractmethod

class ControleRemoto(ABC):
#classe abstratas com metodos
    @abstractmethod
    def ligar(self):
        
        pass
    def desligar(self):

        pass
class Controle_TV(ControleRemoto):
    #é obrigatorio implementar o metodo porque ele está abstrato

    def ligar(self):
        print('Ligando')

    def desligar(self):
        print('Desligando')



controle = Controle_TV()
controle.ligar()
controle.desligar()
#chamar o metodo


