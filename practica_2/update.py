#AQUEST ARXIU ACTUALITZA UN VALOR 
from conn import *

def update():
    sql_read = """ UPDATE public.vehicles SET vehicle_model='CBR600RR' WHERE vehicle_id=1
    """

    connection.execute(sql_read)
    conn.commit()
    result = connection.rowcount

    print("ID modificada: ", result, "Actualització efectuada correctament.")