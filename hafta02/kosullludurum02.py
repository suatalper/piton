sifre = input("Şİfrenizi Girini : ")
if(sifre == "abc123"):
    print("Kolay Şifre")
elif(sifre == "abc.1235.12412"):
    print("Orta Şİfre")
elif(sifre == "abc,123,1234,12345"):
    print("Zor bir şifre")
else: 
    print("Uygun bir şifre giriniz !")
