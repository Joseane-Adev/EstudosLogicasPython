class Passaro:
    #metodo da classe
    def voar(self):
        print('Voando!')

class Pardal(Passaro):
    def voar(self):
        return super().voar()
    print("Pardal voa!")

class Galinha(Passaro):
    def voar(self):
        print('Galinha não voa!')


#funçao de polimorfismo com herança, o objeto animal herda metodo da classe pai Passaro
def plano_voo(animal):
     animal.voar()

#instanciando as classes

plano_voo(Pardal())
plano_voo(Galinha())