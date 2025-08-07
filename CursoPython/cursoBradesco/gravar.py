arquivo = open('arqText.txt', 'w')

arquivo.write ('Curso Py \n')
arquivo.write('Aula gravar')

arquivo.close()

#leitura arquivo

leitura=open('arqText.txt' , 'r')
print(leitura.read())
leitura.close