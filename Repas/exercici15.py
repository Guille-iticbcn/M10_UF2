numbers = []

while True:
    num = int(input("Introdueix un número (0 per acabar): "))
    
    if num == 0:
        break  
    else:
        numbers.append(num)

sorted_tuple = tuple(sorted(numbers))

print("Tupla ordenada:", sorted_tuple)
