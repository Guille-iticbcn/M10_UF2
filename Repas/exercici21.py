numeros_usuari = input("Introdueix 10 números separats per espais: ").split()

numeros = [int(num) for num in numeros_usuari]

suma_total = sum(numeros)
mitjana = suma_total / len(numeros)

numeros.append(suma_total)
numeros.append(mitjana)

print("\nNúmeros de l'usuari:")
print(numeros_usuari)
print("Llista amb suma i mitjana:")
print(numeros)
print("Suma total:", suma_total)
print("Mitjana:", mitjana)
