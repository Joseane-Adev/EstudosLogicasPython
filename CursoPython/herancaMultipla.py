class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas
    
    def __str__(self):
     return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"



class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave( Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero):
    pass



class Onitorrinco(Mamifero,Ave):
    def __init__(self, cor_bico, cor_pelo, numero_patas):
        print(Onitorrinco.__mro__)
        super().__init__(cor_bico=cor_bico,cor_pelo=cor_pelo, numero_patas=numero_patas)

   
#gato = Gato(4, 'PRETO')
#print(gato)

oni=Onitorrinco(numero_patas= 2, cor_pelo="laranja", cor_bico="branco")
print(oni)