def veriekleme():
    dosya = open("veri.txt", "a")
    while True:
        veri = input("Veriyi giriniz:")
        dosya.write(veri)
        secim = input(
            "Veri eklemye devam etmek için 1'e basınız çıkmak için herhangi bir şeye basınız "
        )
        if secim == "1":
            continue
        else:
            break


def verilistele():
    dosya = open("veri.txt", "r")
    veri = dosya.readlines()
    for i in veri:
        print(i)


while True:
    secim = input(
        "Veri eklemek için 1'e basınız verileri listelemek için 2'ye basınız:"
    )
    if secim == "1":
        veriekleme()
    elif secim == "2":
        verilistele()
    else:
        print("Hatalı giriş yaptınız")
