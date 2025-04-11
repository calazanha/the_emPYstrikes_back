import os
import time
import datetime
import calendar

print("Diretório atual:", os.getcwd())
print("Data e hora atual:", datetime.datetime.now())
print("Calendário do mês atual:")
print(calendar.month(datetime.datetime.now().year, datetime.datetime.now().month))
print("Esperando 3 segundos...")
time.sleep(3)
print("Fim da pausa."
