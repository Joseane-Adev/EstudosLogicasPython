def conta_vogais(texto):
    # TODO: Defina um conjunto de vogais tanto minúsculas quanto maiúsculas:
    vogais = ['A','E','I','0','U', 'a', 'e','i','o','u']  
    contador = 0
    # TODO: Inicialize um contador para contar as vogais:
  
  
    # Iteramos pelos caracteres da string
    for char in texto:
       if char in vogais:
         contador += 1
      
# Verifique se o caractere atual é uma vogal e incremente o valor do contador:
    return contador

# Solicitamos ao usuário que insira uma string
texto = input("INSIRA UMA PALAVRA: ")

# Chamamos a função conta_vogais e exibimos o resultado
resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}") 