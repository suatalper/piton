# Program aşağıdaki işlemleri gerçekleştirmelidir:

# Kullanıcıdan adını girmesini isteyiniz.

# Kullanıcıya pizza boyutunu sorunuz: küçük, orta veya büyük.

# Her pizza boyutunun fiyatını kullanıcıdan alınız.

# Örneğin: küçük boy fiyatı, orta boy fiyatı, büyük boy fiyatı kullanıcıdan girilecektir.

# Kullanıcıya içecek isteyip istemediğini sorunuz.

# Eğer kullanıcı "E" veya "e" girerse, içecek fiyatını kullanıcıdan alarak toplam fiyata ekleyiniz.

# Kullanıcının seçimine göre toplam fiyatı hesaplayınız.

# Kullanıcının adını, seçtiği pizza boyutunu, içecek isteyip istemediğini ve toplam tutarı ekrana yazdırınız.

# Kullanıcı geçersiz bir pizza boyutu girerse, uyarı mesajı veriniz ve varsayılan olarak küçük boy pizza fiyatını hesaplayınız.

username = input("Kullanıcı Adınızı Giriniz : ")
boyut = input("Pizza Boyunu giriniz (Küçük,Orta,Büyük) : ")

if(boyut =="Küçük" or boyut == "küçük" or boyut == "Orta" or boyut == "orta" or boyut == "Büyük" or boyut == "büyük"):

    fiyat = input("aldığınız pizzanın fiyatını giriniz fiyatını giriniz : ")
    iceceksecim = input("İçicek İster misiniz ? isterseniz E veya e girini : ")

    if(iceceksecim == "E" or iceceksecim =="e"):
        icecekfiyat = input("İçecek fiyatını giriniz : ")
        iceceksecim = "var"
        fiyat = int(fiyat)+int(icecekfiyat)
        metin = "Kullanıcı Adınız : {}. Seçtiğiniz pizza boyutu {}. İçecek {}. Toplam Tutar : {}."
        yazi = metin.format(username,boyut,iceceksecim,fiyat)
        print(yazi)
else :
    print("Geçersiz bir giriş yaptınız ! ")

