frase = input("Introdueix una frase: ")

fraseSenseEspais = frase.replace(" ", "")

senseRepetits = set(fraseSenseEspais)

tupla = tuple(senseRepetits)

print(''.join(tupla))
