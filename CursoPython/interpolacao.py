nome = "Joseane"
age = 31
profissão = 'programadora'
linguagem = "python"
saldo = 23.145

# interpolaçao old style %
print("Olá, me chamo %s. Tenho %d anos, atualmente sou estudadnte de programação. " \
"Quero ser %s em %s" % (nome, age, profissão, linguagem))

#metodo format
dados = {"nome": "Ana", "age" : 31}

print("Nome: {} Idade: {}".format(nome, age))
print("Nome: {1} Idade: {0}".format(nome, age))
print("Nome: {nome} Idade: {age}".format(**dados))
print("--------------------------")

print(f"Olá me chamo {nome}, tenho {age} anos.Sou {profissão} em {linguagem}. Meu saldo: {saldo:10.2f}")


#fatiamento string

nome = 'Joseane'

print(nome[1])

print(nome[0:6])
print(nome[3:7])
print(nome[4:7])
print(nome[4:7:2])
print(nome[4:7:1])
print(nome[0:7:4])
print(nome[0:7:1])
print(nome[0:7:2])
print(nome[-1])
print(nome[::-1])

#STRING MULTIOPLAS LINHAS
print("_______________________________")
nome = "Ane Alves"

msg = f'''
Olá, meu nome é {nome}, estou aprendendo python.
'''
print(msg) 


print(
    '''
    _____________MENU_____________

    1- DEPOSITAR
    2- SACAR
    3- SAIR
    _______________________________

    OBRIGADO POR USAR O SISTEMA!

    '''    
)