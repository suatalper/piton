menu = {}
while True:
    secim = input(
        "menuye yemek ekelmeek için 1 e e basınız sipariş vermek için 2 ye basınız: "
    )

    if secim == "1":
        while True:
            yemekad = input("Yemeğin adını giriniz :")
            yemekfiyat = input("Yemeğin fiyatını grininiz")
            menu[yemekad] = int(yemekfiyat)

            secim = input("Ekleme yapmaya devam etmek için 1 e basınız")
            if secim == "1":
                continue
            else:
                print(menu)
                break

    elif secim == "2":
        toplamfiyat = 0
        print(menu)
        siparis = input("Ne yemek isterseniz ? ")
        if siparis in menu:
            fiyat = menu[siparis]
            toplamfiyat += fiyat
        else:
            print("Bu menude mevcut değil")
    else:
        print("hatalı giriş yaptınız ")
        continue
