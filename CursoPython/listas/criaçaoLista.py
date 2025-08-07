frutas = ['maça', 'uva']

frutas1 = []

letras = list('python')

#formas de criar listas

# Acessar as listas diretamente

print(frutas[0])

#listas aninhadas

matriz = [
    [2, 'A'],
    ['B', 3],
    [10, "ANE"]
]

print(matriz[2] [-1])
print(matriz[0][1])

#Fatiamento

lista = ['p', 'y','t','o']

print(lista[0:])
print(lista[:2])
print(lista[0:3])
print(lista[0:2:2])
print(lista[::-1])

#iterar listas

loja = ["batom","sombra", "gloss"]

for loja in loja:
    print(loja)

#Enumerate

loja =["batom","sombra", "gloss"]

for indice , loja in enumerate(loja):
    print(f'{indice}: {loja}')

#compreensão de listas 
#filtro 2

numeros = [1, 10, 2, 3, 4]
pares = [number for number in numeros if number %2 == 0]
print(pares)