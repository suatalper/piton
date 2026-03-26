ders_liste = [[],[],[]]
while True :
    ders_adi = input("Ders adınız giriniz : ")
    ders_liste[0].append(ders_adi)
    ders_kredisi = input("Dersin kredisini giriniz :")
    ders_liste[1].append(ders_kredisi)
    ders_kod = input("Ders kodunu giriniz :")
    ders_liste[2].append(ders_kod)

    durum = input("Ders ekleminiz bittiyse 'Evet yazınız'")
    if (durum.lower() == "evet"):
        sayac = len(ders_liste[0])
        for i in range(sayac):
            print(f"Ders ismi : {ders_liste[0][i]} | Ders kredisi : {ders_liste[1][i]} | Ders Kodu : {ders_liste[2][i]}")
        break
    else: 
        continue