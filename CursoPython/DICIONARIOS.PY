dados = {"name": "Ane", "idade": 31, "telefone":"333-555"}

print(dados["idade"])
print(dados["telefone"])

#Sobrescrever os valores
dados["name"] = "Carlos"
print(dados)
#dados["idade"] = 21
#dados["telefone"]= 123-456



#chave aninhada

contatos = {
    "anealves@gmail.com":{"nome": "Ane", "idade": 31},
    "aneal@gmail.com":{"nome": "Ana", "idade": 32},
    "aneves@gmail.com":{"nome": "Carla", "idade": 23},
}

#acessar dicionario
#print(contatos["aneves@gmail.com"]["nome"])

#iterar os itens do dicionario
for chave in contatos:
    print(chave, contatos[chave])




