def meuGerador(numeros: list[int]):
    
    contador += 1
    for numero in numeros:
      yield numeros[contador]* 2

for i in meuGerador(numeros =[1,2,3]):
    print(i)

# gerador = quando o codigo for simples 
#iterador = quando precisar um aestrutira de dados maior