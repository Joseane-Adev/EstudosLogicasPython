numeros =set([ 2,5,6,6,7,7,1])
print(numeros)

frutas =set("morango")
print(frutas)

#set sem a palavra,use a {}

numero ={ 1,1,2,2,3,5,6}

numero = list(numero)

print(numero[2])

#iterar o set
carro = {"gol", "celta", "palio"}

for carros in carro:
    print(carros)

#funçao enumerate
carro = {"gol", "celta", "palio"}

for indice, carros in enumerate(carro):
    print(f'{indice}:{carros}')

#metodos set

conjunto_a ={1,2,3}
conjunto_b ={4,5,6}

conjuntos = conjunto_a.union(conjunto_b)
numeros1 = conjunto_a.intersection(conjunto_b)
diferença = conjunto_a.difference(conjunto_b)
print("Conjuntos unidos:",conjuntos)
print("Intercedem:",numeros1)
print('Diferença',diferença )

conjunto_a ={1,2,4}
conjunto_b ={4,5,6,2,3}

elemento_conjunto = conjunto_a.issubset(conjunto_b)
print(elemento_conjunto)


sorteio ={1,10,15,23,12,11,2,3}
sorteio.add(5)
print(sorteio)

print(len(sorteio))
print(13 in sorteio)