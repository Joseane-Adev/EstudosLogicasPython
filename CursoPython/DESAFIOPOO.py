#TODO: Crie uma classe para converter temperaturas de Celsius para Fahrenheit e um método que realiza o cálculo de conversão:
class ConversorTemperatura:
  
  def celsius_para_fahrenheit(self):
    return (celsius * 9/5) + 32
    
# Entrada do usuário
celsius = float(input())

# TODO: Crie uma instância do conversor:

conversor = ConversorTemperatura()

fahrenheit = conversor.celsius_para_fahrenheit()
print(fahrenheit)