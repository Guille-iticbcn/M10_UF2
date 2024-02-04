from create_table import *
from create import *
from read import *
from delete import *
from update import *

#AQUEST ARXIU CREA UN MENÚ I CRIDA A LES FUNCIONS D'ALTRES ARXIUS PER FER EL CRUD

#FUNCIONS DEL MENÚ
def mostrar_menu(opciones):
    print('Selecciona una opció:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opció: ')) not in opciones:
        print('Opció incorrecta, torni a intentar-ho.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

#CONFIGURACIÓ DEL MENÚ
def menu_principal():
    opciones = {
        '1': ('CREATE TABLE', createTable),
        '2': ('CREATE VEHICLE', create),
        '3': ('READ TABLE', read),
        '4': ('UPDATE VEHICLE', update),
        '5': ('DELETE VEHICLE', delete),
        '6': ('Sortir', salir)
    }
    generar_menu(opciones, '6')


def salir():
    print('Sortint')


if __name__ == '__main__':
    menu_principal()