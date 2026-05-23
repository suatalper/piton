while True:
    secim = input(
        "Mülk Verisi Girmek İçin (1)\n Mülk Araması Yapmak İçin\n Kampanyaya Dahil Mülkleri Görüntelmek için (3)"
    )
    if secim == 1:
        while True:
            ilanno = input("İlan numarasını giriniz : ")
            sehir = input("Şehir ismini giriniz : ")
            ilantür = input("Satılıksa(1), Kiralıksa(2) ' ye basınız : ")
            if ilantür == 1 or 2:
                if ilantür == 1:
                    ""
                else:
                    ""
            else:
                print("Hatalı giriş yaptınız !")

    elif secim == 2:
        ""
    elif secim == 3:
        ""
    else:
        print("Hatalı giriş yaptınız !")
        continue

while True:
    ilanno = input("İlan numarasını giriniz : ")
    sehir = input("Şehir ismini giriniz : ")
    ilantür = input("Satılıksa(1), Kiralıksa(2) ' ye basınız : ")
    if ilantür == 1 or 2:
        if ilantür == 1:
            ""
        else:
            ""
    else:
        print("Hatalı giriş yaptınız !")
