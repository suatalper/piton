# Bir marketten alışveriş yapan kişi
# ürünler almaktadır.
# Aldığı ürünlerin birim fiyatı ve kdv oranı ise ürün üstünde yazmaktadır

# Aldığı ürün katogorisi kozmetik ise  %5 indirim
# detarjan ise %3 zamlı alakmaktadır

# ALdığı ürün sayısı belirsiz olan müşteri
# alışverişi bittiğinde kaç paralık alışveriş yapmıştır

# ürün fiiyatı bir fonksiyonda hesaplanrı ürün fiyatının ve aldığı ürün syaısını
# ekrana yazdırınız


def hesapla(birim_fiyat, birim_adet, kdv, katogori):
    hesap = birim_fiyat * birim_adet
    hesap = hesap + (hesap * kdv / 100)

    if str(katogori).upper() == "DETERJAN":
        hesap = hesap + (hesap * 3 / 100)
        return hesap
    elif str(katogori).upper() == "KOZMETİK":
        hesap = hesap - (hesap * 5 / 100)
        return hesap
    else:
        print("Geçersiz bir katogori girişi yaptınız")


toplam_fiyat = 0

while True:

    fiyat = int(input("Ürün fiyatını giriniz "))
    kdvorani = int(input("KDV oranını giriniz"))
    sayi = int(input("Ürünün adedini giriniz"))
    kat = int(input())
