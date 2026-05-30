import sqlite3

restoran = {}
parcalalist = []
toplamfiyatKS = 0
sayacKS = 0


def devam_etmek_istiyor_mu(sorumetni):
    cevap = input(f"{sorumetni} (Evet / E)").upper()
    if cevap in ["EVET", "E"]:
        return True
    else:
        return False


while True:
    secim = input(
        "--- RESTORAN GÜN SONU PANELİ ---\n1 - Günlük Adisyon Verilerini Sisteme Yükle (.txt'den Sözlüğe)\n2 - Özel Tatlı (Künefe/Sütlaç) Analizi Raporu\n3 - Şanslı Masa Hesaplaması ve Garson Ciroları\n4 - Gün Sonu Kapanış (Ciroları Veritabanına Kaydet ve Çık)\nSeçiminiz:"
    )
    if secim == "1":
        try:
            with open("gunluk_adisyon.txt", "r", encoding="utf-8") as dosya:
                for satir in dosya:
                    temizsatir = satir.strip()
                    if temizsatir != "":
                        parcalalist = temizsatir.split("|")
                        if len(parcalalist) >= 4:
                            restoran[parcalalist[0].upper()] = [
                                parcalalist[1].upper(),
                                parcalalist[2].upper(),
                                parcalalist[3].upper(),
                            ]
                if len(restoran) > 0:
                    print("Değerler başarıyla yüklendi !")
                    continue
                else:
                    print("Bir hata oluştu !")
                    break
        except FileNotFoundError:
            print("Adisyon bulunamadı !")
            break

    elif secim == "2":
        for detaylar in restoran.values():
            if detaylar[1] == "SÜTLAÇ" and "KÜNEFE":
                sayacKS += 1
                bulunan_fiyat = int(detaylar[2])
                toplamfiyatKS += bulunan_fiyat

        ort = toplamfiyatKS / sayacKS
        print(f"Künefe ve Sütlaç Yiyen Masaların fiyat ortalması {ort}")
    elif secim == "3":
        sesliharf = ["eıoüaiöu"]
        sesliharf_say = 0
        sessizharf_say = 0
        for yemek_detaylari in restoran.values():
            for yemekler in yemek_detaylari[1]:
                for harf in yemekler:
                    if harf in sesliharf:
                        sesliharf_say += 1
                    else:
                        sesliharf_say += 1
            if sessizharf_say > sesliharf_say:
                indirimlifiyat = yemek_detaylari[1] - yemek_detaylari * 0.15
                restoran[yemek_detaylari[0]][2] = indirimlifiyat
                print("Bu Masaya indirim uygulanmıştır !")

    elif secim == "4":
        baglanti = sqlite3.connect("restoran.db")
        imlec = baglanti.cursor()
        imlec.execute("""
        CREATE TABLE IF NOT EXISTS GunlukSatislar (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        garson_adi TEXT,
        toplam_ciro INTEGER)
                      """)
        toplamciro = 0
        garson_ciro = {}
        for detaylist in restoran.values():
            garsonadi = detaylist[0]
            fiyat = detaylist[2]
            if garsonadi in garson_ciro:
                garson_ciro[garsonadi] += fiyat
            else:
                garson_ciro[garsonadi] += fiyat

        for garson, toplamfiyat in garson_ciro.items():
            imlec.execute(
                "INSERT INTO GunlukSatislar (garson_adi, toplam_ciro) VALUES (?, ?)",
                (garson, toplamfiyat),
            )
        baglanti.commit()
        baglanti.close()

        print("Veritabanı işlemi tamamlandı!")
        break
