kayitListesi = []
while True:

    envanter = []
    OyuncuSepet = []

    def ekleme():
        OyuncuSepet.append(playername)
        OyuncuSepet.append(playerid)
        OyuncuSepet.append(server)
        OyuncuSepet.append(envanter)
        kayitListesi.append(OyuncuSepet)

    playername = input("Envantere hoşgeldiniz ! \n Lütfen Kullanıcı adınızı giriniz :")
    playerid = input("ID'nizi giriniz : ")
    server = input("Hangi sunucda bulunuyorsunuz ? : ")

    print("Lütfen envanteriniz için 4 adet eşya giriniz.")
    for i in range(4):
        item = input(f"{i+1}. Item ekleyiniz: ")

        envanter.append(item)

    durum = input("Kullanıcı eklemey devam etmek istiyormusunuz ? :")
    if durum.upper() == "EVET":
        ekleme()
        continue
    else:
        ekleme()
        print("--- Avrupa sunucusundaki insanlar ---")

        for arserver in kayitListesi:
            if "AVRUPA" in  arserver[2].upper():
                print(arserver)

        print("--- Harf Kontrolü ---")

        sesli_harfler = "aeıioöuü"
        for oyuncu in kayitListesi:
            playername = oyuncu[0]
            envanter = oyuncu[3]
            for item in envanter:
                sesliharf = 0
                sessizharf = 0
                for harf in item :
                    if harf in sesli_harfler:
                        sesliharf += 1 
                    else:
                        sessizharf += 1
                if sesliharf > sessizharf:
                    print(f"Sesli harf sayısı sessizden fazla olan kullanıcı : {playername} \n Ve İtemi {item}")
                else:
                    print("Sesli harf sayısı sessizden fazla olan yok ")
        break
