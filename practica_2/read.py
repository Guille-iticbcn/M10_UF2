#AQUES ARXIU FA UN PRINT DELS VALORS D'UNA TAULA
from conn import *

def read():
    sql_read = """ SELECT vehicle_id, vehicle_tipus, vehicle_pes, vehicle_marca, vehicle_color, vehicle_model
                    FROM public.vehicles
    """

    connection.execute(sql_read)

    result = connection.fetchall()

    for i in result:
        print("vehicle_id: ", i[0],)
        print("vehicle_tipus: ", i[1],)
        print("vehicle_pes: ", i[2],)
        print("vehicle_marca: ", i[3],)
        print("vehicle_color: ", i[4],)
        print("vehicle_model: ", i[5], "\n")
        