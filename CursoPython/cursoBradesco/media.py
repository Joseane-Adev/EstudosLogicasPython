nota1 = float(input("digite sua primeira nota: "))
nota2 = float(input("digite sua segunda nota: "))

#calcular media
mediafinal = (nota1 + nota2) / 2

#verificar

if mediafinal >= 7.0:
    print("Sua média é : ", mediafinal, "Aprovado")

elif mediafinal == 5.0:
    print("Sua média é: ", mediafinal, "Recuperação")
else:
    print("Sua média é: ", mediafinal, "Reprovado")