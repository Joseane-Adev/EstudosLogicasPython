class Pessoa:
    def __init__(self, nome = None, idade = None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_pela_data_nascimento(cls, ano, mes, dia, nome):
        
        idade = 2025 - ano
        return cls(nome, idade)
       #cls = é a referencia da classe, preciso ter acesso ao contexto da classe usamos esse metodo 


    #metodo estatico
    #nao precico nem de contexto, nem de classe e nem da instancia do objeto esse é o metodo.
    @staticmethod
    def maior_idade(idade):
        return idade >= 18
    
#p = Pessoa('Ane', 31)
#print(p.nome, p.idade)

p1 = Pessoa.criar_pela_data_nascimento(1994, 5, 21, 'Ane')
print(p1.nome, p1.idade)

#chamar o metodo estatico, chama a classe e depois o metodo
print(Pessoa.maior_idade(31))