kayitListesi = []

while True:
    envanter = []
    OyuncuSepet = []

    playername = input("Envantere hoşgeldiniz ! \n Lütfen Kullanıcı adınızı giriniz :")
    playerid = input("ID'nizi giriniz : ")
    server = input("Hangi sunucda bulunuyorsunuz ? : ")

    print("Lütfen envanteriniz için 4 adet eşya giriniz.")
    for i in range(4):
        item = input(f"{i + 1}. Item ekleyiniz: ")

        envanter.append(item)

    durum = input("Kullanıcı eklemey devam etmek istiyormusunuz ? :")
    if durum.upper() == "EVET":
        OyuncuSepet = [playername, playerid, server, envanter]
        kayitListesi.append(OyuncuSepet)
        continue
    else:
        OyuncuSepet = [playername, playerid, server, envanter]
        kayitListesi.append(OyuncuSepet)
        break

print("--- Avrupa sunucusundaki insanlar ---")

for arserver in kayitListesi:
    if "AVRUPA" in arserver[2].upper():
        print(arserver)

print("--- Harf Kontrolü ---")

sesli_harfler = "aeıioöuü"
for oyuncu in kayitListesi:
    sayac = 0
    playername = oyuncu[0]
    envanter = oyuncu[3]

    for item in envanter:
        # DÜZELTME 1: Sayaçlar HER YENİ EŞYADA (item) sıfırlanmak üzere buraya alındı.
        sesliharf = 0
        sessizharf = 0

        for harf in item:
            if harf.isalpha():
                if harf.lower() in sesli_harfler:
                    sesliharf += 1
                else:
                    sessizharf += 1

        # DÜZELTME 2: Kelimenin harfleri bitti, şartı kontrol ediyoruz. (for harf ile aynı hizada)
        if sessizharf > sesliharf:
            sayac += 1

    # DÜZELTME 3: Oyuncunun tüm eşyaları bitti, sonucu 1 kere ekrana basıyoruz. (for item ile aynı hizada)
    if sayac > 0:
        print(
            f"{playername} adlı kullanıcının itemlerindeki sessiz harf sayısının sesliyi geçen toplam {sayac} adet itemi vardır"
        )
    else:
        print("Sesli harf sayısı sessizden fazla olan yok")
