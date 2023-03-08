

def sisseastumine(taotlejad:list,hinded:list):
    n = int(input("Sisestage taotlejate arv: "))
    for i in range(n):
        nimi = input("Sisestage taotleja nimi: ")
        hinne = float(input("Sisestage taotleja punktisumma: "))
        taotlejad.append(nimi)
        hinded.append(hinne)

def astunud_inimeste(taotlejad:list,hinded:list):
    p = int(input("Sisestage taotlejate arv: "))
    print(f"Taotlejate loend riigist {p}:")
    for i in range(p):
        print(f"{i+1}. {taotlejad[i]} – {hinded[i]} punkti")

def sorteerimine(taotlejad:list, hinded:list):
    print("Taotlejate nimekiri tähestikulises järjekorras:")
    for nimi, hinne in sorted(zip(taotlejad, hinded)):
        print(f"{nimi} - {hinne} punktid")

def Leia_inimest(taotlejad:list, hinded:list):
    b = int(input("Sisestage halvimate tulemuste arv: "))
    s = sorted(hinded)
    print(f"Loetelu {b} kõige halvemate tulemustega taotlejast:")
    for i in range(b):
        index = hinded.index(s[i])
        print(f"{i+1}. {taotlejad[index]} - {s[i]} punktid")

def avr(taotlejad:list, hinded:list):
    avg = sum(hinded) / len(hinded)
    print(f"Taotlejate keskmine punktisumma: {avg}")

def delete_taotleja(taotlejad:list, hinded:list):
    taotleja=input("Sisesta taotleja kes sa tahad kustuta: ")
    if taotleja in taotlejad:
            ind=taotlejad.index(taotleja)
            taotlejad.pop(ind)
            hinded.pop(ind)
            print(taotlejad,hinded)
    else:
        print("Vale opilane")
    return taotlejad,hinded
