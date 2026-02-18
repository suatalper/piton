isim = input("İsminizi giriniz :")
yas = input("Yaşınızı giriniz : ")
yazi = "Merhaba ben {},{} yaşındayım"

metin = yazi.format(isim,yas)

print(metin)