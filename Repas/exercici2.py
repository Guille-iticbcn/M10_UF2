valor1 = float(input("Introdueix el preu "))

valor2 = float(input("Introdueix l'IVA (4%, 10%, 21%) "))

if (valor2 == 4 or valor2 == 10 or valor2 == 21):
    print("IVA: ")
    print(valor2)
    print("Import amb IVA: ")
    print(valor1 + (valor1 * valor2 / 100))
    #print('IVA: '  valor2  ' Import amb IVA: '  valor1 + (valor1 * valor2 / 100))
else:
    print("Error, l'IVA que has introduït no es correcte.")