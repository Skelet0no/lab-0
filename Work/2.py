nn = input()
wwod = nn.lower() + " "
while nn != "":
    nn = input()
    if nn == "":
        break
    wwod += nn.lower() + " "
wwod = wwod.split(" ")
del wwod[-1]
bukvi = {}
for i in wwod:
    bukvi[i[-1].upper()] = []
wwod = list(set(wwod))
for i in wwod:
    for j in i[::-1]:
        if j.upper() in list(bukvi.keys()):
            if i.lower() not in bukvi[j.upper()]:
                bukvi[j.upper()].append(i.lower())
                break

for i in bukvi.keys():
    print(f"{i} - ", end="")
    print(*sorted(bukvi[i]), sep=", ")