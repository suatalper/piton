def devam_etmek_istiyor_mu(sorumetni):
    cevap = input(f"{sorumetni} (Evet / E)").upper()
    if cevap in ["EVET", "E"]:
        return True
    else:
        return False


mülk = {}
while True:
    mülk.clear()
    secim = input(
        " Mülk Verisi Girmek İçin (1)\n Mülk Araması Yapmak İçin (2)\n Kampanyaya Dahil Mülkleri Görüntelmek için (3)\n Çıkış için (4)"
    )
    if secim == "1":
        son_ilan_no = 100
        try:
            with open("ilan_kayitlari.txt", "r", encoding="utf-8") as dosyaD:
                for satir in dosyaD:
                    temiz_satir = satir.strip()
                    if temiz_satir != "":
                        parcalarlist = temiz_satir.split(",")
                        son_ilan_no = int(parcalarlist[0])
        except FileNotFoundError:
            pass
        while True:
            son_ilan_no += 1
            sehir = input("Şehir ismini giriniz : ")
            fiyat = int(input("Fiyatı giriniz : "))
            ilantür = input("Satılıksa(1), Kiralıksa(2) ' ye basınız : ")
            if ilantür in ["1", "2"]:
                if ilantür == "1":
                    mülk[son_ilan_no] = [sehir, fiyat, ilantür]
                else:
                    mülk[son_ilan_no] = [sehir, fiyat, ilantür]
                cevap = devam_etmek_istiyor_mu("Veri eklemek istiyormusunuz ? ")
                if not cevap:
                    with open("ilan_kayitlari.txt", "a", encoding="utf-8") as dosya:
                        for son_ilan_no, bilgiler in mülk.items():
                            sehirD = bilgiler[0]
                            fiyatD = bilgiler[1]
                            ilantürD = bilgiler[2]
                            if ilantürD == "1":
                                ilantürD = "SATILIK"
                                dosya.write(
                                    f"{son_ilan_no},{sehirD},{fiyatD},{ilantürD}\n"
                                )
                            else:
                                ilantürD = "KİRALIK"
                                dosya.write(
                                    f"{son_ilan_no},{sehirD},{fiyatD},{ilantürD}\n"
                                )
                    break
                else:
                    continue
            else:
                print("Hatalı giriş yaptınız !")
                continue
    elif secim == "2":
        mülkler = {}
        with open("ilan_kayitlari.txt", "r", encoding="utf-8") as dosya:
            for satir in dosya:
                temiz_satir = satir.strip()
                if temiz_satir != "":
                    ilanLİST = temiz_satir.split(",")
                    mülkler[ilanLİST[0]] = [ilanLİST[1], ilanLİST[2], ilanLİST[3]]
        secim = input(
            "Arama kısmına hoş geldiniz ! \n Şehire Göre Aramaa yapmak için (1) \n Fiyata Göre Arama Yapmak için (2) \n İlanın Türüne Göre yapmak için (3)"
        )
        if secim == "1":
            sehirA = input(
                "Hangi Şehirdeki ilanları listelemek istersiniz ? : "
            ).upper()
            for ilanno, bilgiler in mülkler.items():
                if sehirA in bilgiler[0].upper():
                    print(
                        f"İlan Numarası : {ilanno} // Şehir : {bilgiler[0]} // Fiyat : {bilgiler[1]} // İlan Türü {bilgiler[2]}"
                    )
        elif secim == "2":
            fiyatMİN = int(input("Minumumun fiyatı giriniz :"))
            fiyatMAX = int(input("Maximum fiyatı giriniz :"))
            sayac = 0
            for ilanno, bilgiler in mülkler.items():
                if fiyatMİN <= int(bilgiler[1]) <= fiyatMAX:
                    print(
                        f"İlan Numarası : {ilanno} // Şehir : {bilgiler[0]} // Fiyat : {bilgiler[1]} // İlan Türü {bilgiler[2]}"
                    )
                    sayac += 1
                else:
                    continue
            if sayac == 0:
                print("Aradığınız kritere uygun ilan bulunmamaıştır ! ")
        elif secim == "3":
            ilantürA = input("Satılık ilanlar için (1) \n Kiralık İlanlar için (2) :")
            for ilanno, bilgiler in mülkler.items():
                if ilantürA == "1":
                    if bilgiler[2] == "SATILIK":
                        print(
                            f"İlan Numarası : {ilanno} // Şehir : {bilgiler[0]} // Fiyat : {bilgiler[1]} // İlan Türü {bilgiler[2]}"
                        )
                elif ilantürA == "2":
                    if bilgiler[2] == "KİRALIK":
                        print(
                            f"İlan Numarası : {ilanno} // Şehir : {bilgiler[0]} // Fiyat : {bilgiler[1]} // İlan Türü {bilgiler[2]}"
                        )
                else:
                    print("Hatalı giriş yaptınız !")
                    continue

        else:
            print("Hatalı giriş yaptınız !")
            continue
    elif secim == "3":
        mülk3 = {}
        with open("ilan_kayitlari.txt", "r", encoding="utf-8") as dosya:
            for satir in dosya:
                temiz_satir = satir.strip()
                if temiz_satir != "":
                    ilanLİST = temiz_satir.split(",")
                    mülk3[ilanLİST[0]] = [ilanLİST[1], ilanLİST[2], ilanLİST[3]]

        print("\n>>> SİSTEM MESAJI: ÖZEL İNDİRİM KAMPANYASI BAŞLATILDI <<<")
        print("---------------------------------------------------------")
        print("[!] Hedef: 2.000.000 TL üzerindeki tüm Satılık portföyler.")
        print("[!] İşlem: Sistemdeki fiyatlar %5 indirimle güncelleniyor...")
        print("---------------------------------------------------------")
        print("Kampanyaya uyan ilanlar:\n")
        for ilanno, bilgiler in mülk3.items():
            if bilgiler[2] == "SATILIK":
                if int(bilgiler[1]) > 2000000:
                    indirimlifiyat = int(bilgiler[1]) - int(bilgiler[1]) * 0.05
                    print(
                        f"İlan Numarası : {ilanno} // Şehir : {bilgiler[0]} // İndirimli Fiyat : {indirimlifiyat} // İlan Türü {bilgiler[2]}"
                    )
                else:
                    print("Henüz Kampanyaya uygun ilan yüklenmemiştir !")

            else:
                print("Henüz Kampanyaya uygun ilan yüklenmemiştir !")

    elif secim == "4":
        print("Çıkılıyor...")
        break
    else:
        print("Hatalı giriş yaptınız !")
        continue
