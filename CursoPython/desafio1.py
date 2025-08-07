def paridade(numero):
    return "Par" if numero % 2 == 0 else "Impar"

print(paridade(2))
print(paridade(5))
print(paridade(6))

#meu exemplo
numero = int(input("Digite um numero:"))

divisão = numero % 2

if divisão == 0:
  print("Par")
else:
  print("Ímpar")



def verificador_ano_bissexto():
    ano = int(input('digite um ano: '))

    if ano % 4 and ano % 400:
      print("Sim")
    else:
      print("Não")

# TODO: Verifique se o ano é bissexto utilizando uma estrutura de controle condicional, como if/else:

verificador_ano_bissexto()