# bir markete giden öğrenci
# 5 tane poğaça ve 3 simit almaktadır.cebindeki kredi kartı
# limiti kendi yaşının ve geldiği ilin plaka koduunun çarpımı kadar 
# alan öğrenci cebinde artan para var mı ? yoksa borçlandımı

# simit ve poğaça float değerdedir

yas = input("Yaşınızı giriniz :")
plakano = input("Geldiğiniz ilin plaka nosunu girin:")
limit = int(yas)*int(plakano)

simitadtfiyat = input("Simitin fiyatı ne kadar :")
pogacaadtfiyat = input("Poğaça fiyatını ne kadar :")  

simitfiyat = float(simitadtfiyat)*3
pogacafiyat = float(pogacaadtfiyat)*5
toplamfiyat = simitfiyat +pogacafiyat


if limit < toplamfiyat:
    print("Limit yetersiz")
else:
    print("Bakiye yeterli\n Kalan Paranız : ")
    print(limit-toplamfiyat)
    