from conn import * 

#AQUI ES CREARA LA TAULA EN LA BASE DE DADES.
def createTable():
    sql_create_table = ''' CREATE TABLE vehicles(
                vehicle_id SERIAL PRIMARY KEY,
                vehicle_tipus VARCHAR(255) NOT NULL,
                vehicle_pes INT NOT NULL,
                vehicle_marca VARCHAR(255) NOT NULL,
                vehicle_color VARCHAR(255) NOT NULL,
                vehicle_model VARCHAR(255) NOT NULL
    )'''

    print(sql_create_table)
    connection.execute(sql_create_table)
    print(connection)
    conn.commit()