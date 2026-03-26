# Senaryo: "Akıllı Otopark Yönetim Sistemi"
# Bir alışveriş merkezinin otoparkı için küçük bir takip yazılımı geliştirmeniz isteniyor. Sistemin işleyiş kuralları şunlardır:
# 1.	Sabit Kat Bilgileri: Otoparkın kat isimleri sabittir ve değiştirilemez. Bu bilgileri bir demet (tuple) içinde tutun: katlar = ("Zemin Kat", "1. Kat", "2. Kat")
# 2.	Araç Listesi: Otoparka giriş yapan araçların plakalarını tutmak için boş bir liste oluşturun.
# 3.	Giriş İşlemi: Kullanıcıdan input() ile araç plakası alın.
#           o	Eğer kullanıcı "çıkış" yazarsa veri girişi durmalı ve mevcut liste ekrana yazdırılmalıdır.
#           o	Eğer otoparktaki araç sayısı 5'e ulaşmışsa, "Otopark dolu, araç alınamaz!" uyarısı verilmeli ve döngü sonlanmalıdır.
# 4.	Kontrol: Girilen plaka eğer daha önce listeye eklenmişse (içerideyse), "Bu araç zaten içeride!" uyarısı verilmeli ve tekrar eklenmemelidir.
# 5.	Özet: İşlem bittiğinde, otoparkın hangi katlara sahip olduğunu (demetten çekerek) ve içerideki araçların listesini for döngüsü kullanarak ekrana yazdırın.

katlar = ("Zemin Kat", "1. Kat", "2. Kat")
plaka_list = []


while True:
    if len(plaka_list) == 5:
        print("Otopark dolu !")
        break
    else:
        plaka = input("hoşgeldiniz girmek için aracınızız plakanızı giriniz : ")
    if plaka in plaka_list:
        print("Bu araç zaten içerde !")
    else:
        plaka_list.append(plaka)

    durum = input(
        "Çıkmak için 'Çıkış' yazınız  devam etmek iin herhanagi bir tuşa basınız :"
    )
    if durum.lower() == "çıkış":
        cikis_plake = input("Çıkacak olan aracın plakasını giriniz : ")
        if cikis_plake in plaka_list:
            plaka_list.remove(cikis_plake)
            for i in range(len(plaka_list)):
                print("Otoparktaki mevcut araçlar .", plaka_list[i])
            break
        else:
            print("Girdiğiniz plaka mecut değil !")
            continue
    else:
        continue
