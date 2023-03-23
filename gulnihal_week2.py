#soru1
ad=input("Ogrencinin Adi:")
soyad=input("Ogrencinin Soyadi:")
ogrenciNo=input("Ogrencinin Numarasi:")

ders=1
sonuc=""
while ders<5:
    ders_=input("Lutfen ders ismini giriniz:")
    ders_vize=int(input("Lutfen vize notunuzu giriniz:"))
    ders_final=int(input("Lutfen final notunuzu giriniz:"))
    ortalama=(ders_vize+ders_final)/2
    if ortalama>=50:
        cikti="gectiniz"
    else:
        cikti="kaldiniz"
    a=(f"{ders_} dersinden {ortalama} ile {cikti}\n")
    sonuc+=a
    ders+=1
print(f"{ogrenciNo} nolu ogrenci {ad} {soyad}")
print(sonuc)

#soru2
sayilar=[42,29,17,15,10,9,6,4,2,1]
ortalama=(42+29+17+15+10+9+6+4+2+1)/10

yuksek=0
dusuk=0

for i in sayilar:
    if i >ortalama:
        yuksek+=1
    else:
        dusuk+=1

print("Yuksek sayilarin sayisi:",yuksek)
print("Dusuk sayilarin sayisi:",dusuk)  

#soru3
while True:
    sayi1=int(input("Lutfen bir baslangic sayisi giriniz:"))
    sayi2=int(input("Lutfen bir bitis sayisi giriniz:"))
    if sayi2<sayi1:
        print("Lutfen baslangic sayiniz bitis sayinizdan kucuk olsun.")
    elif sayi1<sayi2:
        break
    else:
        continue
    
toplam=0
i= sayi1
while i <=sayi2:
    if i%2==1:
        toplam+=i
    i+=1

print("Girdiginiz araliktaki tek sayilarin toplami:",toplam)

    
