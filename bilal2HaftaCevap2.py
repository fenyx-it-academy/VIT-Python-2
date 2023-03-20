#Soru-2 : Aşağıdaki listede bulunan sayıların ortalamasını 
# hesaplayan bir Python programı yazın. 
# Daha sonra, listedeki her bir sayıyı,
# ortalamadan büyük olanlar "yuksek", 
# ortalamadan küçük olanlar "dusuk" olarak ayıran 
# bir "for" döngüsü ekleyin ve her bir grubun sayısını ekrana yazdırın.
sayilar = [42, 29, 17, 15, 10, 9, 6, 4, 2, 1]
yuksek=[]
dusuk=[]
toplam=0
for i in sayilar:
    toplam+=i
ortalama=toplam/len(sayilar)
print ("ortalama : ",ortalama)
for i in sayilar:
    if i<ortalama:
        dusuk.append(i)
    elif i>ortalama:
        yuksek.append(i)
print("Ortalamadan dusuk olan",len(dusuk),"sayı var.")
print("bu sayılar",dusuk)
print("Ortalamadan yüksek olan",len(yuksek),"sayı var.")
print("bu sayılar",yuksek)
