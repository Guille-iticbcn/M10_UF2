#AQUEST ARXIU ELIMINA UNA CONSULTA DE LA TAULA
from conn import *

sql = """ DELETE FROM public.vehicles WHERE vehicle_id=1
"""

connection.execute(sql)
conn.commit()