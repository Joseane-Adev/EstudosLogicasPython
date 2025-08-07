#DECLARAR A FUNÇÃO
def exibir_mensagem():
    print('OI')

#CHAMAR A FUNÇÃO
#exibir_mensagem()

#funçao exibir nome
def exibir_nome(nome):
    print(f'ESSE NOME É:  {nome}')

#exibir_nome(nome="joseane")

#retorna lista de numeros

def calcular_total(numeros):
    return sum(numeros)

print(calcular_total([10,5]))

#argumentos nomeados

def salvar_carros(marca, modelo,ano):
    print(f"CARRO INSERIDO NA LISTA:  {marca} / {modelo} /{ano}")

(salvar_carros( marca= "Fiat", modelo="Palio", ano=1994))

#args e kwargs
def exibir_poema(dta_extenso, *args, **kwargs):
    texto = "\n" .join(args)
    meta_dados = "\n" .join([f"{chave.title()}:{valor}"for chave, valor in
    kwargs.items()])
    msg = f"{dta_extenso}\n{texto}\n\n{meta_dados}"
    print(msg)

exibir_poema(
    "08-06-2-25",
    "tentativa python",
    "dominando funçoes",
     autor= "Joseane",
     ano= 2025
)

#função parte 2

def calculo(a,b):
    return a * b

def exibir_calculo(a,b, funcao):
    resultado = funcao(a,b)
    print(f"O resultado da multiplicação {a} * {b} = {resultado}")

exibir_calculo(5, 4, calculo)

teste = calculo
print("O teste é" ,teste(2,20))

#escopo local e global

salario = 1200

def calcular_salario(bonus):
    #informe que a variavel é global
    global salario
    salario += bonus
    return salario

print(calcular_salario(500))