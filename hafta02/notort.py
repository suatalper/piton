# bir sınıftaki öğrencinin dönem ortalması eğer 2.0 üstünde olursa
# üstten 6 kredi ders alabilliyor eğer 3.0 üsstünde olursa 10 kredi alabiliyor
# öğrenci dönemde 2 ders alıyor. ve bu dersler 15 er kredi derslerin sıvaları %40 vize 
# %60 final olarak not ortalması alınıyor . dönem sonunda not ortalması yukardaki koşullara göre ayarlansın
# sınavın not dönüşümü ortalama 100-85 arasındaysa 4 84-70 arasındayasa 3 69-50 arasındaysa 2 alarak
# 50-0 arasındaysa 1 olaraka hesaplanır 

ders1vize = input("İlk dersin vize notunuzu giriniz : ")
ders1final = input("İlk dersin finalini giriniz :")

ders2vize = input("İkinici dersin vizesini giriniz :")
ders2final = input("ikinci dersin finali giriniz :")

ders1 = float(ders1vize)*0.4 + float(ders1final) *0.6
ders2 = float(ders2vize)*0.4 + float(ders2final)*0.6
 
notort = (ders1 + ders2)/2
ort = notort/25

kredi = 30
if(ort >= 2.0 ):
    kredi = kredi + 6.0
    metin = "Krediniz : {} AKTS. Not Ortalamanız {}"
    txt = metin.format(kredi,ort)
    print(txt)

elif(ort >= 3.0):
    kredi = kredi + 10.0
    metin = "Krediniz : {} AKTS. Not Ortalamanız {}"
    txt = metin.format(kredi,ort)
    print(txt)
elif (ort <= 2.0):
    metin = "Krediniz : {} AKTS. Not Ortalamanız {}"
    txt = metin.format(kredi,ort)
    print(txt)
