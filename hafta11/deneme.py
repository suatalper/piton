# Kullanıcının elindeki hisse veya kripto paraların miktarını ve bunların anlık/sanal fiyatlarını kullanarak toplam servetini hesaplayan bir finansal araç.
# Sözlük (Dictionary) Kullanımı: Burada birden fazla sözlük kullanman gerekecek.
# cuzdan: Kullanıcının sahip olduğu varlıklar ({"BTC": 0.5, "ETH": 2.0, "AVAX": 50}).
# fiyatlar: Varlıkların güncel birim fiyatları ({"BTC": 65000, "ETH": 3200, "AVAX": 40}).
# Fonksiyon (Function) Kullanımı: Sistemin yönetimi için fonksiyonlar yazmalısın:
#  varlik_ekle(cuzdan, coin_adi, miktar),
# varlik_sat(cuzdan, coin_adi, miktar)
# ve iki sözlüğü karşılaştırarak (elindeki miktar * anlık fiyat) toplam dolar değerini hesaplayan toplam_bakiye_hesapla(cuzdan, fiyatlar).
