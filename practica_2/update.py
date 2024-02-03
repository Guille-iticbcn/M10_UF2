#AQUEST ARXIU ACTUALITZA UN VALOR 
from conn import *

sql = """ UPDATE public.vehicles SET vehicle_model='CBR600RR' WHERE vehicle_id=1
"""

connection.execute(sql)
conn.commit()
result = connection.rowcount

print("ID modificada: ", result, "Actualització efectuada correctament.")