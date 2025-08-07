#criando tuplas

frutas=("laranja", 'uvA',)

letras = tuple("maçã")

loja = ("gloss",)

numeros = tuple([1,2,3])

#acesso direto tupla

frutas[0]
frutas[-1]

#tuplas aninhadas

matriz = [
    [1, 2, 'a']
    ['b', 'c', 3]
]
matriz[0]
matriz [0][2]

def soma_tupla(tupla):

    return sum(tupla)

soma_tupla[1,2,3]