class Pessoa:
    def __init__(self, name, ano_nascimento):
        self._name = name
        self._ano_nascimento = ano_nascimento

#para retornar o nome
    @property
    def name(self):
      return self._name
    
    #retornar idade
    @property
    def age(self):
       _ano_atual = 2025

       return _ano_atual - self._ano_nascimento




pessoa = Pessoa('Ane', 1994)
print(f'Nome: {pessoa.name} \tIdade: {pessoa.age}')