#READLINE() - lÊ uma linha por vez
#readlines() - retorn a lista onde cada elemento é uma linha do arquivo

#arquivo = open("C:\Users\Usuário\Desktop\CursoPython\Arquivos", "r")
#print(arquivo.read())
#arquivo.close()

#print(arquivo.readline())

#nao funcionou

#ESCREVENDO EM UM ARQUIVO

#WRITE - 
#WRITELINES()

arq = open("C:\\Users\\Usuário\\Desktop\\CursoPython\\Arquivos\\teste.txt", "w")

arq.write("Escrevendo no novo arquivo!")
arq.writelines(' Python')
arq.close