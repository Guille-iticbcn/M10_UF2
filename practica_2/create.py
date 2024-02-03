from conn import *

#AQUEST ARXIU CREA UNA CONSULTA A LA NOSTRA TAULA VEHICLES.
sql_insert = """ INSERT INTO public.vehicles
                    (vehicle_id, vehicle_tipus, vehicle_pes, vehicle_marca, vehicle_color, vehicle_model)
                    VALUES 
                    ('1', 'Moto', '210', 'Honda', 'Vermell', 'CBR650R')"""

connection.execute(sql_insert)
conn.commit()