def verificador_ano_bissexto():
    ano = int(input('digite um ano: '))
    resultado = ano % 4 and 400

    if resultado == 0 :
      print("Sim")
    else:
      print("Não")

# TODO: Verifique se o ano é bissexto utilizando uma estrutura de controle condicional, como if/else:

verificador_ano_bissexto()