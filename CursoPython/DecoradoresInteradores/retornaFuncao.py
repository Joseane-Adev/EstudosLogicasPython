
def calculadora(operacao):
    def soma(a, b):
        return a + b   

    def subtrair(a, b):
        return a - b  

    def multiplicar(a, b):
        return a * b

    def dividir(a, b):
        return a / b

    # tipo um switch case (match-case disponível a partir do Python 3.10)
    match operacao:
        case '+':
            return soma
        case '-':
            return subtrair
        case '*':
            return multiplicar
        case '/':
            return dividir

op = calculadora("/")
print(op(10,5))

#codigo não funciona
