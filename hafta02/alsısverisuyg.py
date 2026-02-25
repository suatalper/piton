print("Alışveriş Sİtemize Hoş geldiniz Lütfen Kullanı adınızı ve şirenizi belirleyiniz !")
kullanici_adi = input("Kullanıcı Adınızı Giriniz :")
sifre = input("Şifenizi giriniz ve karakter uzunluğu 40 karakteri geçmemli :")

if( len(sifre) >= 40 ):
    print("Şİfre Çok uzun !")
else:
    print("Başarıyla giriş yaptınız !")