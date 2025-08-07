#decorador de Log

from datetime import datetime
def log_transaçao(funcao):
    def wrapper(*args, **kwargs):
        data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:')
        print(f'[{data_hora}] Executando transação: {funcao.__name__}')
        resultado = funcao(*args, **kwargs)
        return resultado
    return wrapper

#funçao d etransaçao

@log_transaçao
def deposito(valor):
    print(f'Depositando R$: {valor}')

@log_transaçao
def saque(valor):
    print(f'Sacando R$: {valor}')

@log_transaçao
def criar_conta(nome):
    print(f'Criando conta para {nome}')


#teste
deposito(200)
saque(50)
criar_conta('Ana')
