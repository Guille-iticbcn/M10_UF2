#AQUEST ARXIU ELIMINA UNA CONSULTA DE LA TAULA
from conn import *

def delete():
    sql_delete = """ DELETE FROM public.vehicles WHERE vehicle_id=1
    """

    connection.execute(sql_delete)
    conn.commit()