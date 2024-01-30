nums = input("Introdueix 10 número separats per espais: ")

numbers = [int(num) for num in nums.split()]

sorted_tuple = tuple(sorted(numbers))

print("Tupla ordenada:", sorted_tuple)
