from conn import * 

#AQUI ES CREARA LA TAULA EN LA BASE DE DADES.
sql = ''' CREATE TABLE vehicles(
            vehicle_id SERIAL PRIMARY KEY,
            vehicle_tipus VARCHAR(255) NOT NULL,
            vehicle_pes INT NOT NULL,
            vehicle_marca VARCHAR(255) NOT NULL,
            vehicle_color VARCHAR(255) NOT NULL,
            vechicle_model VARCHAR(255) NOT NULL
)'''

print(sql)
connection.execute(sql)
print(connection)
conn.commit()