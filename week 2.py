#1.Sorunun Cevabı



-----------------------------------------------------------------------
#2. Sorunun Cevabı
sayilar=[42,29,17,15,10,9,6,4,2,1]
ortalama=sum(sayilar)/len(sayilar)
dusuk=0
yuksek=0
print("Sayıların Ortalaması: ",ortalama)
for i in sayilar:
    if i<ortalama:
        print(i,"Ortalamadan Düşük")
        dusuk+=1
    elif i>ortalama:
        print(i,"Ortalamadan Büyük")
        yuksek+=1
print("Ortalamadan Düşük:  ",dusuk,"  sayı var")
print("Ortalamadan Yüksek:  ",yuksek,"  sayı var")

--------------------------------------------------------------
#3. Sorunun Cevabı

while True:
    sayi1=int(input("1.sayıyı giriniz:  "))
    sayi2=int(input("2.sayıyı giriniz:  "))
    toplam=0
    if sayi1>sayi2 or sayi1==sayi2 or sayi2==sayi1+1:
       print("Geçersiz Giriş yaptınız Lütfen Tekrar Giriş Yapınız")
       continue
    else:
        while sayi1<sayi2:
            sayi1+=1
            if sayi1%2>0:
                    toplam+=sayi1
                    print(sayi1)
    print("2 Sayı arasındaki tek sayıların toplamı: ",toplam)
    break
