num = -1
num0 = 0

while (num < 10 or num > 100):
    num = int(input("Escriu un número entre el 10 i el 100: "))

tupla_numeros = tuple(range(1, num + 1))

print(tupla_numeros)