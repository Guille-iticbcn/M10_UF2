paraula1 = input("Introdueix la primera paraula: ")
paraula2 = input("Introdueix la segona paraula: ")

tupla = tuple(paraula1 + paraula2)

numLletres = {}
for lletra in tupla:
    numLletres[lletra] = numLletres.get(lletra, 0) + 1

for lletra, quantitat in numLletres.items():
    print(f"{lletra}: {quantitat}")
