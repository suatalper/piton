rektorluk = input("Rektıorluk :")
isim = input("İsminiz:")
bolum =input("Bölümünüz:")
anablmdalı = input("Ana bilim dalını girniniz")
ders = input("Ders :")
kredi = input("Kredi :")

metin ="""{} Rekterlüğüne\n{} bölümü {} ana bilim dalı öğrencinizim.\n
        Ders kayıtlarında yaşanan aksiliklerden dolayı {} dersimin kredisini {} olarak işaretledim.\n
        kredilerin düzeltilmesiin talep ediyorum."""

yazi = metin.format(rektorluk,bolum,anablmdalı,ders,kredi)

print(yazi)