# Création d'une liste d'entiers
entiers = [1, 2, 3, 4, 5]

# Conversion de la liste en bytearray
byte_array = bytearray(entiers)


index = entiers.index(3)
byte_array[index] = 10

print(byte_array)