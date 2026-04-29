import sqlite3

vereitabani = sqlite3.connect("kitap.db")
imlec = vereitabani.cursor()

sorgu = "create table if not exists Siparis (TcNo,KitapAdi,Fiyat)"
imlec.execute(sorgu)
vereitabani.commit()

sorgu2 = "insert into Siparis Values('1111','Sefiller','250')"
imlec.execute(sorgu2)
vereitabani.commit()

sorgu3 = "SELECT * FROM Siparis"
imlec.execute(sorgu3)
veri = imlec.fetchall()
print(veri)
for i in veri:
    print(list(i)[1])
