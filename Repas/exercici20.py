diccionari_contactes = {}

while True:
    nom = input("Introdueix el nom (o escriu 'para' per parar): ").capitalize()

    if nom.lower() == 'para':
        break

    if nom in diccionari_contactes:
        print("Aquest nom ja existeix al diccionari. Introdueix un altre nom.")
        continue

    edat = input("Introdueix l'edat: ")

    diccionari_contactes[nom] = int(edat)

print("\nDiccionari de contactes:")
print(diccionari_contactes)
