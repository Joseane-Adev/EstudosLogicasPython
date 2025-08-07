from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = '2025-7-4 18:44'

hora_pt = '%d/%m/%Y %a'
hora_en = '%Y-%m-%d %H:%M'

#formTANDO DATA E HORA para o pt-Brasil

print('Data Brasil: ',data_hora_atual.strftime(hora_pt))

data_convertida =datetime.strptime(data_hora_str, hora_en)
print(data_convertida)