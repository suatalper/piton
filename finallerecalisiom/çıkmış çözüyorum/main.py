import sqlite3

uye = {}


def uye_Kaydet_Vt(gelen_sozluk):
    baglanti = sqlite3.connect("otobus.db")
    imlec = baglanti.cursor()
    sorgu = "create table if not exists Uyeler (Tc text, Ad text,Soyad text,Sifre text,Yas integer,Mail text,Durum text)"
    imlec.execute(sorgu)

    for tcno, val in gelen_sozluk.items():
        ad = val[0]
        soyad = val[1]
        sifre = val[2]
        yas = int(val[3])
        mail = val[4]
        durum = val[5]

    imlec.execute(
        "insert into Uyeler values (?,?,?,?,?,?,?)",
        (tcno, ad, soyad, sifre, yas, mail, durum),
    )
    baglanti.commit()
    baglanti.close()

    return 1


def uye_ol():
    bilgiler = input(
        "Lütfen TC numaranızı , Adınızı, Soyadınızı, Şifrenizi, Yaşınızı, Mail Adrsinizi ARAYA VİRGÜL KOYUCAK ŞEKİLDE GİRİNİZ :"
    )
    bilgiler_list = bilgiler.split(",")
    temiz_bilgiler_list = []
    for kirli in bilgiler_list:
        temiz = kirli.strip()
        temiz_bilgiler_list.append(temiz.upper())
        if 23 > int(temiz_bilgiler_list[4]):
            kullanci_tipi = "Öğrenci".upper()
        else:
            kullanci_tipi = "Normal".upper()

        temiz_bilgiler_list.append(kullanci_tipi)

    uye[temiz_bilgiler_list[0]] = temiz_bilgiler_list[1:]

    islem_sonucu = uye_Kaydet_Vt(uye)

    if islem_sonucu == "1":
        print("İşlem başarılı !")
    else:
        print("İşlem Başarısız !")


def giris_yap():
    kullancı_adi = input("Kullanıcı Adınızı giriniz :")
    sifre = input("Şifrenizi giriniz :")

    baglanti = sqlite3.connect("otobus.db")
    imlec = baglanti.cursor()
    sorgu = "select * from Uyeler where tcno = ? , sifre = ?"
    imlec.execute(sorgu(kullancı_adi, sifre))

    basarli_mi = imlec.fetchone()

    if basarli_mi is not None:
        print("Giriş Başarılı !")
    else:
        print("Şifre veya kullancı adı hatalı ")


def cikis_yap():
    pass


while True:
    secim = input("1-Üye olun \n2-Giriş Yapın \n3-Çıkış Yapın \nSeçim : ")
    if secim == "1":
        uye_ol()
    elif secim == "2":
        giris_yap()
    elif secim == "3":
        pass
    else:
        print("Hatalı seçim yaptınız ")
        continue
