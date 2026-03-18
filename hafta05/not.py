not_listesi = []
while True:
    ders = input("Ders ismini giriniz :")
    not_listesi.append(ders)
    durum = input("Ders ekleme bitti mi bittiyse 'evet' yazınız : ")

    if(durum.lower()  == "evet"):
        del not_listesi[0]

        for i in range(len(not_listesi)):
            print(not_listesi[i])

        break
    else:
        continue