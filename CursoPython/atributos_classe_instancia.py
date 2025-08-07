class Estudante:
    escola = "DIO"
    #variavel de classe

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        #variaveis de instancia, quando tem self

    def __str__(self):
        return f'{self.nome}, matricula : {self.matricula} estudante da {self.escola}'

std = Estudante('Ane', 12345)
print(std)