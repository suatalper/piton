# Senaryo: "Dijital Kantin Sıra Yönetimi"
# Okul kantininde yoğunluğu önlemek için bir sipariş takip sistemi kurmanız isteniyor. Sistem şu adımlara göre çalışmalıdır:
# 1.	Stok Listesi: Kantinde o an satışı yapılan ürünleri içeren bir liste oluşturun:
# urunler = ["Tost", "Ayran", "Simit", "Çay"]
# 2.	Sipariş Toplama: Boş bir siparis_listesi oluşturun.
# 3.	Süreç: Kullanıcıdan sürekli olarak sipariş etmek istediği ürünü girmesini isteyin.
#   o	Kullanıcı "onayla" yazarsa sipariş alma işlemi durmalı ve fiş yazdırılmalıdır.
#   o	Kullanıcı listede olmayan bir ürün girerse: "Üzgünüz, [ürün_adı] stokta yok!" uyarısı verilmeli ve listeye eklenmemelidir.
#   o	Kullanıcı listede olan bir ürün girerse: "Siparişe eklendi." denilmeli ve ürün siparis_listesine eklenmelidir.
# 4.	Kısıtlama: Bir kişi tek seferde en fazla 4 ürün sipariş edebilir. 4. ürün eklendiğinde sistem otomatik olarak siparişi sonlandırmalı ve fişi yazdırmalıdır.
# 5.	Özet (Fiş): Program bittiğinde, toplam kaç ürün sipariş edildiğini ve ürünlerin isimlerini for döngüsü kullanarak ekrana yazdırın.

urunler = ("Tost", "Ayran", "Simit", "Çay")
siparis_listesi = []
while True:
    if 4 == len(siparis_listesi):
        print("En fazla 4 ürün eklenebilir")
        break
    else:
        print("Hoş geldiniz ürünlerimiz aşağıdadır :")
        for i in range(len(urunler)):
            print(urunler[i])
        siparis = input("Siparişinizi giriniz : ")
        if siparis in siparis_listesi:
            print("Bu ürün zaten eklenmiş")
