# Bir banka müşterisi para trasnferi yapmak istiyor 
# transfer türünü seçen kişi eğer trasnfer adresi TR 9954 ile başlıyorsa
# İş bankası heasabıdır. aynı banka trasnferinde ücret kesilmeyecekdir ama farklı bankalarda 
# yüzde 1 lik kısmı kadar banka komisyon almaktadır buna güre transfer türünü ve ne kadar para ilettiğini yazan ve 
# gönderi ücretini yazdıran kod. Eğer müşterinin yaşı 19-22 yaşlarında arasındyasa para alınmıyor 
# son durumu eran yazdırırınız. 

isim = input("İsminizi giriniz :")
yas = int(input("Yaşınızı giriniz"))
banka_isim = input("Bankanızın ismini giriniz :")
banka_g_isim = input("Gönderilcek banka ismini giriniz :")
para = int(input("Göndermek istediğiniz para miktarını giriniz :"))
alici = input("Alıcı ismini giriniz :")
if(banka_g_isim == banka_isim):
    metin = "Gönderen : {}. Alıcı : {}. Gönderilcek para miktarı : {}, Alınan Komisyon : yok"
    print(metin.format(isim,alici,para))
else:
    if(18 >= yas and 20 <= yas):
         metin = "Gönderen : {}. Alıcı : {}. Gönderilcek para miktarı : {}, Alınan Komisyon : yok"
         print(metin.format(isim,alici,para))
    else:
         metin = "Gönderen : {}. Alıcı : {}. Gönderilcek para miktarı : {}, Alınan Komisyon : {} "
         komisyon = 
         print(metin.format(isim,alici,para,komisyon))
        