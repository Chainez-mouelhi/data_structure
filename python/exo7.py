liste = [1, 2,3,4,5,6,7,8,9]
x = input ( "nb de rotation")

new_liste = liste[int(x):] + liste[0:int(x)]
print(new_liste)