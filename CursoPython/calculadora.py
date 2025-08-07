#definir as funçoes
#dois parametros
def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    return x / y

#função calculadora

def calculadora():
    print("----Calculadora Python----")
    print("Escolha o operador")
    print(" +  Somar")
    print(" - Subtrair")
    print(" * Multiplicar")
    print(" / Dividir")

    escolha = input('Digite o operador escolhido: ')

    try:
        num1 = int(input("Digite um  numero: "))
        num2 = int(input('Digite um segundo numero: '))
    except ValueError:
        print("Digite a penas numeros inteiros")

    #condiçoes do operador

    if escolha == "+":
        print(f'O resultado é: ', somar(num1, num2))
    elif escolha == "-":
        print(f'O resultado é: ', subtrair(num1, num2))
    elif escolha == "*": 
        print("O resultado é: ",multiplicar(num1, num2))
    elif escolha == "/":
        print("O resultado é: ", dividir(num1,num2))
    else: 
        print("Inválido")



calculadora()

    
    

