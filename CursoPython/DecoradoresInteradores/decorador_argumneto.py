def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print('faz algo antes de executar')
        resultado = funcao(*args, **kwargs)
        print('faz algo depois de executar')
        return resultado
    
    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f'ola mundo {nome}')
    return nome.upper()


#chama a funçao
resultado = ola_mundo('Joao')
print(resultado)
print(ola_mundo.__name__)

#introspecção = capacidade do objeto saber sobre os proprios atributos em tempo de execução
