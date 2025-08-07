
from datetime import datetime, timezone, timedelta
#nao funcionou o pytz

#sem pytz
data_oslo =datetime.now(timezone(timedelta(hours=2)))
data_sp = datetime.now(timezone(timedelta(hours=-3)))

print('Hora e data Oslo: ',data_oslo)
print('Hora e data São paulo: ', data_sp)
