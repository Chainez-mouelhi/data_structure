liste = [1, 1, 2, 2, 2, 2, 2, 2, 2]
liste2 =[]
for nombre in liste:
    if nombre not in liste2:
        liste2.append(nombre)

print(liste2)