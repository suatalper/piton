fiyatlist=[]
adlist=[]
adetlist=[]
fiyat_ad_adet = [fiyatlist,adlist,adetlist]
günsonufiyat = 0

while True:
    fiyat = input("Birim fiyatını girinniz : ")
    ad = input("Ürünün adını giriniz : ")
    adet = input("Adedini giriniz : ")

    toplamfiyat= int(adet)*int(fiyat)
    fiyatlist.append(toplamfiyat)
    adlist.append(ad)
    adetlist.append(adet)

    durum = input("Bittiyse lütfen evet yazınız : ")
    if(durum.lower()  == "evet"):
        for i in range(len(fiyatlist)):
            günsonufiyat = fiyatlist[i] + günsonufiyat
        print("Gün sonu harcanan para {}".format(günsonufiyat))
        break
    else:
        continue