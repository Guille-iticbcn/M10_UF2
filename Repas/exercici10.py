import random

num = random.randint(0,100)
sapElNum = False
numIntents = 0

while (sapElNum == False):
    adivina = int(input("Entra el numero: "))
    if(adivina > num):
        print(f'El número és més petit que {adivina}.')
        numIntents += 1
    elif (adivina < num):
        print(f'El número és més gran que {adivina}.')
        numIntents += 1
    else:
        print(f'Has adivinat el número! Ho has intentat {numIntents} vegades.')
        sapElNum = True