fiyat = float(input("ürünün fiyatını griniz: "))
indirim_yuzdesi = float(input("indirim yüzdesini giriniz: "))
indirim_tutari = fiyat *  indirim_yuzdesi / 100
indirimli_fiyat = fiyat -indirim_tutari
print("indirim tutarı:",indirim_tutari ,"TL")
print("indirimli fiyat:",indirimli_fiyat,"TL")
