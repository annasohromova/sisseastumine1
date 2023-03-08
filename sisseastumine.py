from module1 import *
taotlejad = []
hinded = []
sisseastumine(taotlejad,hinded)
while True:
        print("\nValige toiming:\n1. Tutvu taotlejate nimekirjaga\n2. Kuvage tähestikulises järjekorras inimeste loend ja nende tulemused\n3. Leidke n inimest, kellel on kõige halvemad tulemused\n4. Leidke taotlejate keskmine punktisumma\n5. Eemalda taotlejate nimekirjast\n6. Välju")
        menu = int(input("Sisestage toimingu number: "))
        if menu == 1:
            astunud_inimeste(taotlejad,hinded)
        elif menu == 2:
            sorteerimine(taotlejad,hinded)
        elif menu == 3:
            Leia_inimest(taotlejad,hinded)
        elif menu == 4:
            avr(taotlejad,hinded)
        elif menu == 5:
            delete_taotleja(taotlejad,hinded)
        elif menu == 6:
            print("Programmist väljumine...")
            break
        else:
            print("Viga: vale valik.")
