# while True :
#  ad = input("Kütüphanenemizin arama motoruna hoş geldiniz aradığınız kitabın ismini giriniz : ")
#  yazar = input("Yazarın adını giriniz :")


# kitapno = input("Kitap numarsını giriniz (Max 5 hane) : ")

while (True) :
    prompt = input("Aradığınız cümleyi yazın")
    kelime = prompt.split(' ')
    for i in kelime:
        if len(i) >= 5:
            print(i,"Kelimesi uygun")
        else:
            print(i,"Kelimesi uygun değil")
    durum = input("Devam için evet yazınız")
    if(durum.lower () == "evet"):
        continue
    else :
        break