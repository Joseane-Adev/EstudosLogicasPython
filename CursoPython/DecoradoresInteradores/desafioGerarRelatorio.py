from datetime import datetime

#para amrmazenar as transaçoes
historico = []

def log_transaçao(funcao):
    def wrapper(*args, **kwargs):
        data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        print(f'[{data_hora}] Executando transação: {funcao.__name__}')
        tipo_transacao = funcao.__name__
        resultado = funcao(*args, **kwargs)

        # salvando a transação no histórico
        historico.append({'data_hora': data_hora,'tipo': tipo_transacao,'detalhes': resultado})

        # log na tela
        print(f'[{data_hora}] Transação concluída: {tipo_transacao}')
        return resultado  # importante retornar o resultado da função original

    return wrapper  # ← ESSENCIAL: precisa retornar o wrapper


#funçao detransaçao

@log_transaçao
def deposito(valor):
    print(f'Depositando R$: {valor}')

@log_transaçao
def saque(valor):
    print(f'Sacando R$: {valor}')

@log_transaçao
def criar_conta(nome):
    print(f'Criando conta para {nome}')

#GERADOR DE RELATORIO

def gerar_relatorio(tipo=None):
    for transacao in historico:
        if tipo is None or transacao['tipo'] ==tipo:
            yield transacao

#uso
deposito(1200)
saque(100)
deposito(300)
criar_conta('Maria')
saque(10)

print('\n-- Relatorio completo--')
for transacao in gerar_relatorio():
    print(transacao)

print('\n--- Apenas saques---')
for transacao in gerar_relatorio(tipo='saque'):
    print(transacao)