import random

numero_aleatorio = random.randint(1,100)
tentativas = 0
escolha_jogador = int(input("Digite um numero qualquer entre 1 e 100: "))

if escolha_jogador <= 20 : 
    print("Quase, foi perto!")
elif escolha_jogador <= 60:
    print("Foi por pouco, não desista")
else:
    print("Está mais perto!")



while escolha_jogador != numero_aleatorio:
    tentativas += 1
    if escolha_jogador < numero_aleatorio:
        print("Tente outra vez um numero maior!")
    else:
        print("Tente ou numero menor!")
    escolha_jogador = int(input('Tente novamente: '))


tentativas += 1
print(f'Parabéns, você acertou em {tentativas} tentativas!')
