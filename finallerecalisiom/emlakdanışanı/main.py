def devam_etmek_istiyor_mu(sorumetni):
    cevap = input(f"{sorumetni} (Evet / E)").upper()
    if cevap in ["EVET", "E"]:
        return True
    else:
        return False


mülk = {}
while True:
    secim = input(
        " Mülk Verisi Girmek İçin (1)\n Mülk Araması Yapmak İçin\n Kampanyaya Dahil Mülkleri Görüntelmek için (3)\n Çıkış için (4)"
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
            with open("ilan_kayitlari.txt", "r", encoding="utf-8") as dosyaD:
                for satir in dosyaD:
                    temiz_satir = satir.strip()
                    parcalarlist = temiz_satir.split(",")

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
                                    f"{son_ilan_no},{sehirD},{fiyatD},{ilantürD}"
                                )
                            else:
                                ilantürD = "KİRALIK"
                                dosya.write(
                                    f"{son_ilan_no},{sehirD},{fiyatD},{ilantürD}"
                                )
                    break
                else:
                    continue
            else:
                print("Hatalı giriş yaptınız !")
                continue

    elif secim == "2":
        with open("ilan_kayitlari.txt", "r", encoding="utf-8") as dosya:
            veri = dosya.readlines()

    elif secim == "3":
        pass
    elif secim == "4":
        print("Çıkılıyor...")
        break
    else:
        print("Hatalı giriş yaptınız !")
        continue
