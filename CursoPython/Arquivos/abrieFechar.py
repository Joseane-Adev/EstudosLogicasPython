#abrir arquivo
file = open('example.txt', 'r')

#escrever arquivo
file = open('example.txt', 'w')

#para anexar conteudo ao arquivo existente
file = open('example.txt' 'a')

#LENDO ARQUIVO----------------

arquivo = open('exemplo.txt', 'r')
print(arquivo.read())
arquivo.close()

#READLINE() - lÊ uma linha por vez
#readlines() - retorn a lista onde cada elemento é uma linha do arquivo

arquivo = open('lorem.txt', 'r')
print(arquivo.readline())
arquivo.close()