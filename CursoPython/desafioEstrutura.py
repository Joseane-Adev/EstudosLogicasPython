# No "TODO", abaixo: Crie a função 'soma_tupla' para receber uma tupla de números inteiros como argumento:

def soma_tupla(tupla):
    
    return sum(tupla)
    
    
if __name__ == "__main__":
    entrada = input()
    lista_strings = entrada.split()
    
# No "TODO", abaixo: Defina tupla para receber os números inteiros:
    elementos = tuple(map(int, entrada.split()))
    
    resultado = soma_tupla(elementos)
    print(f"A soma dos elementos da tupla é: {resultado}")


#desafio 2 explorando conjuntos

# TODO: Crie uma função 'elementos_comuns' que receba duas listas de números inteiros separados por espaço:
def elementos_comuns(lista1,lista2):
  
    set1 = set(map(int,lista1))
    set2= set(map(int,lista2))

    return list(set1.intersection(set2))

# Leitura das listas
lista1 = input().split()
lista2 = input().split()

# Verifica se todas os elementos das listas podem ser convertidos para inteiros
if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    comuns = elementos_comuns(lista1, lista2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")

#DESAFIO3
def contar_caracteres(string):
#TODO: Inicialize um dicionário vazio 'contador' para armazenar as contagens de caracteres.:
  contador = { }
  
#TODO: Itere através de cada caractere na string string.

  for caractere in string:
#TODO: Para cada caractere, verifique se ele já está presente no dicionário contador:
   if caractere in contador:
    contador[caractere]+= 1
   else:
    contador[caractere] = 1
    
  return contador
    

# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)

    
