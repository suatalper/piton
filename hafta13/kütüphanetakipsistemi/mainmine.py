dosya = open("Kitap.txt", "r")
sozluk = {}
for i in dosya:
    veri = i.split(",")
    sozluk.setdefault(veri[0], veri)
