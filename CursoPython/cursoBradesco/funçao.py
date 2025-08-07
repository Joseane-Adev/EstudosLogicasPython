def lerNotas():
    n=float(input('digite uma nota para o aluno'))
    return n


def resultado(n1,n2):

   media = (n1+n2) / 2
   print('NOTA 1: ', n1)
   print('NOTA 2: ', n2)
   print('MÉDIA: ', media, 'RESULTADO: ', end="")
   if media >= 7.0:
       print("Aprovado")
   else:
       print("Recuperação")



a= lerNotas()
b=lerNotas()
resultado(a,b)