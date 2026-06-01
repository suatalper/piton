class Karakter:
    def __init__(self, isim, can, saldirigüci):
        self.isim = isim
        self.can = can
        self.saldirigüci = saldirigüci

    def saldir(self, hedef):
        hedef.can -= self.saldirigüci
        print(
            f"{self.isim}, {hedef.isim} adlı düşmana saldırdı! Hedefin kalan canı: {hedef.can}"
        )


kahraman_isim = input("Kahramanınız ismini giriniz :")
kahraman_can = int(input("Canını giriniz :"))
kahraman_damage = int(input("Kahramanın hasarını giriniz :"))

canavar_isim = input("Canavarın ismini giriniz :")
canavar_can = int(input("Canını giriniz :"))
canavar_damage = int(input("Canavarın hasarını giriniz :"))

secim = input("Saldırmak istiyorsanız 1\nCanları Görmek istiosanız 2 \n")

kahraman = Karakter(kahraman_isim, kahraman_can, kahraman_damage)
canavar = Karakter(canavar_isim, canavar_can, canavar_damage)

if secim == "1":
    kahraman.saldir(canavar)
elif secim == "2":
    pass
else:
    print("Hatalı giriş yaprınız !")
