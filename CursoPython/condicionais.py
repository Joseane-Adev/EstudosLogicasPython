MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input("Qual sua idade? "))

if idade > MAIOR_IDADE:
    print('Maior de idade, pode ter CNH')
elif idade == IDADE_ESPECIAL:
    print('Pode fazer aulas teóricas')
else:
    print("Menor de idade, não pode ter CNH") 

saldo = 2000
saque = 3000

status = "Sucesso" if saldo >= saque else "Não é possivel"

print(f"{status} 'ao realizar o saque")


