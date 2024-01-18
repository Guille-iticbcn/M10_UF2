frase = input("Introdueix una frase: ")

fraseSenseEspais = frase.replace(" ", "")

tupla = tuple(fraseSenseEspais)

print(''.join(tupla))
