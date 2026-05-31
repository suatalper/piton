import math
import sqlite3

jamkayitlari = {}

while True:
    secim = input(
        "--- GAME JAM MUĞLA YÖNETİM PANELİ ---\n1 - Başvuru Verilerini Sisteme Yükle (.txt'den Sözlüğe)\n2 - Platformer Oyunları Bütçe Analizi\n3 - Rektörlük Sponsorluğu Dağıtımı ve Güncelleme\n4 - Veritabanına Kaydet ve Çıkış\nSeçiminiz:"
    )
    if secim == "1":
        with open("takim_basvurulari.txt", "r", encoding="utf-8") as dosya:
            for satir in dosya:
                temizsatir = satir.strip()
                demet_söz_values = ()
                if temizsatir != "":
                    parcalanmi_veriler = temizsatir.split("-")
                    anahtar = parcalanmi_veriler[0].upper()
                    for gelisticiler in parcalanmi_veriler[1].split(",").upper():
                        jamkayitlari[anahtar] = (
                            gelisticiler,
                            parcalanmi_veriler[2].upper(),
                            int(parcalanmi_veriler[3]),
                        )
            print("İşlem başarıyla gerçekleşti !")
    elif secim == "2":
        sayac = 0
        toplambüt = 0
        for key, value in jamkayitlari.items():
            if value[1] in "Platformer".upper():
                sayac += 1
                toplambüt += value[2]
        if sayac > 0:
            ort = math.ceil(toplambüt / sayac)
            print(f"Platformer oyunlarının bütçe ortalaması : {ort}")
        else:
            print("Platformer takım bulunamadı !")
    elif secim == "3":
        gecici_demet = ()
        for key, value in jamkayitlari.items():
            if value[2] > 2000:
                for gelisticiler in value[0]:
                    if len(gelisticiler) % 2 == 0:
                        yeni_bütce = value[2] + value[2] * 0.2
                        jamkayitlari[key] = (value[0], value[1], int(yeni_bütce))

    elif secim == "4":
        baglanti = sqlite3.connect("gamejam.db")
        imlec = baglanti.cursor()
        imlec.execute(
            "CREATE TABLE IF NOT EXISTS FinalKayitlar (TakimAdi TEXT, UyeSayisi INTEGER,SonButce INTEGER )"
        )
        for takim_adi, detaylar in jamkayitlari.items():
            (
                imlec.execute("INSERT INTO FinalKayitlar VALUES (?,?,?) "),
                (takim_adi, len(detaylar[0]), detaylar[2]),
            )
        baglanti.commit()
        baglanti.close()
    else:
        print("Hatalı giriş yaptınız :")
        continue
