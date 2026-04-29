# bir ögrencinin alımış olduğu dersler bir dosyay kaydedilliyor
# Ders adı ders kredi olarak tüm bilgiler bir dosyaya kadyediliyor

dersler = open("dersler.txt", "a", encoding="UTF-8")
while True:
    dersad = input("Dersin adını giriniz : ")
    dersakts = input("Dersin kredisini giriniz :")
    dersler.write("Dersin Adı :" + dersad + "\n" + "Dersin kredisi: " + dersakts)

    secim = input("Ders eklemeye devam etmek için 1 e basınız :")
    if secim == "1":
        continue
    else:
        soru = input("Dersleri görmek için 1 e basınız :")
        if soru == "1":
            dosya = open("dersler.txt", "r")
            veri = dosya.readlines()
            for i in veri:
                print(i)
            break
        else:
            break
