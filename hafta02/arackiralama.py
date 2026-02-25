isim = input("Adınızı giriniz :")
yas = input("Yaşınızı giriniz : ")
tür = input("Kiralamakistediğiniz Araç Türünü giriniz (eko,orta,lüks) : ")
if(tür == "eko" ):
    aracfiyat = input("Aracın Günlük fiyatını giriniz :")
    gün = input("Kaç gün kiralamaya düşünüyorsunuz ? ")
    toplamfiyat = int(aracfiyat)* int(gün)
    if(yas >= "25"):
        toplamfiyat = float(toplamfiyat) + float(toplamfiyat)*0.1
        if(int(gün)>=7):
            toplamfiyat = toplamfiyat - toplamfiyat*0.85
    else :
        if(int(gün)>=7):
         toplamfiyat = toplamfiyat - toplamfiyat*0.85

    metin = "İsim : {}. Yaşı : {}. Araç Tercihi {}. Toplam Fiyat : {}:"
    yazi = metin.format(isim,yas,tür,toplamfiyat)
    print(yazi)

elif(tür == "orta"):
    aracfiyat = input("Aracın Günlük fiyatını giriniz :")
    gün = input("Kaç gün kiralamaya düşünüyorsunuz ? ")
    toplamfiyat = int(aracfiyat)* int(gün)
    if(yas >= "25"):
        toplamfiyat = float(toplamfiyat) + float(toplamfiyat)*0.1
        if(int(gün)>=7):
            toplamfiyat = toplamfiyat - toplamfiyat*0.85
    else :
        if(int(gün)>=7):
         toplamfiyat = toplamfiyat - toplamfiyat*0.85
    metin = "İsim : {}. Yaşı : {}. Araç Tercihi {}. Toplam Fiyat : {}:"
    yazi = metin.format(isim,yas,tür,toplamfiyat)
    print(yazi)
    
elif(tür == "lüks"):
    aracfiyat = input("Aracın Günlük fiyatını giriniz :")
    gün = input("Kaç gün kiralamaya düşünüyorsunuz ? ")
    toplamfiyat = int(aracfiyat)* int(gün)
    if(yas >= "25"):
        toplamfiyat = float(toplamfiyat) + float(toplamfiyat)*0.1
        if(int(gün)>=7):
            toplamfiyat = toplamfiyat - toplamfiyat*0.85
    else :
        if(int(gün)>=7):
         toplamfiyat = toplamfiyat - toplamfiyat*0.85
    metin = "İsim : {}. Yaşı : {}. Araç Tercihi {}. Toplam Fiyat : {}:"
    yazi = metin.format(isim,yas,tür,toplamfiyat)
    print(yazi)