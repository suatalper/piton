lab_malzemesi = []
while True :
    malzeme = input("Malzeme adını giriniz : ")
    if malzeme in lab_malzemesi:
        print("Bu daha önceden eklenmiş")
    else:
        lab_malzemesi.append(malzeme)

    durum = input("Bittiyse lütfen evet yazınız : ")
    if(durum.lower()  == "evet"):
        print("Bu kadar malzeme girilmiştir :",len(lab_malzemesi))
        # for i in range(lab_malzemesi):
        #     print(f"{lab_malzemesi[i]}")
        break
    else:
        continue