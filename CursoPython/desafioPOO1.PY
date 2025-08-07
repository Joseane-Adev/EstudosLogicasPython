num1 = int(input())
num2 = int(input())

class Calculadora:
  
  def soma(self):
   return num1 + num2

# Criando uma instância da calculadora
calc = Calculadora()

resultado = calc.soma()
print(resultado)