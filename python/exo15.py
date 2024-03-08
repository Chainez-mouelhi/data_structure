mon_dict : dict ={"Alice" : 16, "Albert" : 13, "Tom" : 12, "Nono" : 19, "Hugo" : 20}
new_dict : dict ={}

for name, note in mon_dict.items():
    if note >= 15:
        new_dict[name] = note
print(new_dict)