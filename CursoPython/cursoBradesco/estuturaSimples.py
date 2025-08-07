a = input("digite um avalor para variavel a")
b= input("digite um valor para variavel b")

if (a>b):
    aux=a;
    a=b;
    b=aux;

print("O valor da variavel a é: ", a);
print("O valor da variavel b é: " , b);