import json

class Vehiculo:
    def __init__(self, marca, modelo, year, color, tipo_combustible, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self.color = color
        self.tipo_combustible = tipo_combustible
        self.kilometraje = kilometraje

    def obtener_marca(self):
        return self.marca

    def obtener_modelo(self):
        return self.modelo

    def obtener_año(self):
        return self.year

    def obtener_color(self):
        return self.color

    def obtener_tipo_combustible(self):
        return self.tipo_combustible

    def obtener_kilometraje(self):
        return self.kilometraje

    def establecer_marca(self, marca):
        self.marca = marca

    def establecer_modelo(self, modelo):
        self.modelo = modelo

    def establecer_año(self, year):
        self.year = year

    def establecer_color(self, color):
        self.color = color

    def establecer_tipo_combustible(self, tipo_combustible):
        self.tipo_combustible = tipo_combustible

    def establecer_kilometraje(self, kilometraje):
        self.kilometraje = kilometraje

    def mostrar_partes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Tipo de Combustible: {self.tipo_combustible}")
        print(f"Kilometraje: {self.kilometraje} kilómetros")

    def a_diccionario(self):
        return {
            "marca": self.marca,
            "modelo": self.modelo,
            "year": self.year,
            "color": self.color,
            "tipo_combustible": self.tipo_combustible,
            "kilometraje": self.kilometraje
        }

if __name__ == "__main__":
    mi_vehiculo = Vehiculo(marca="Nissan", modelo="GTR R-34", year=1990, color="Azul", tipo_combustible="Gasolina", kilometraje=250000)

    mi_vehiculo.mostrar_partes()

    vehiculo_diccionario = mi_vehiculo.a_diccionario()

    vehiculo_json = json.dumps(vehiculo_diccionario, indent=2)

    print("\nObjeto convertido a JSON:")
    print(vehiculo_json)
