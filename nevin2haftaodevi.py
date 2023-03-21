cevap1

#Kullanıcıdan Adi, Soyadi, Ogrenci Numarasi, 4 ders adi, bu derslerin Vize ve Final notlari istenecektir.
# Vize notunun % 40′ı ile Final Notunun %60′ınin toplamı yil sonu ortalamasini verecektir. 
# Ortalama 50‘den küçükse ekranda “KALDI“, 50 ve üstüyse ekranda “GEÇTİ” yazdırılacaktır.
# Bu yazdirma islemi 4 ders icinde yapilacak ve dersler alt alta yazdirilacaktir.
kullaniciadi=input("Adinizi giriniz:")
soyad=input("Soyadinizi giriniz:")
ogrencino=input("Ogrenci numaranizi giriniz:")
ders1=input("1.Dersinizi Giriniz:").upper()    
ders2=input("2.Dersinizi Giriniz:").upper() 
ders3=input("3.Dersinizi Giriniz:").upper() 
ders4=input("4.Dersinizi Giriniz:").upper() 
drs1vize=float((input("{} Dersinizin vize notunu giriniz:".format(ders1))))
drs1final=float((input("{} Dersinizin final notunu giriniz:".format(ders1))))
drs2vize=float((input("{} Dersinizin vize notunu giriniz:".format(ders2))))
drs2final=float((input("{} Dersinizin final notunu giriniz:".format(ders2))))
drs3vize=float((input("{} Dersinizin vize notunu giriniz:".format(ders3))))
drs3final=float((input("{} Dersinizin final notunu giriniz:".format(ders3))))
drs4vize=float((input("{} Dersinizin vize notunu giriniz:".format(ders4))))
drs4final=float((input("{} Dersinizin final notunu giriniz:".format(ders4))))
drs1ysnotu=int((drs1vize*0.4)+(drs1final*0.6))
drs2ysnotu=int((drs2vize*0.4)+(drs2final*0.6))
drs3ysnotu=int((drs3vize*0.4)+(drs3final*0.6))
drs4ysnotu=int((drs4vize*0.4)+(drs4final*0.6))
if drs1ysnotu>=50:
    sonuc1="GECTI"
else:
    sonuc1="KALDI"
print("{} dersinin vize notu:{},final notu{},yilsonu ortalamasi:{},sonuc:{}".format(ders1,drs1vize,drs1final,drs1ysnotu,sonuc1))
if drs2ysnotu>=50:
    sonuc2="GECTI"
else:
    sonuc2="KALDI"
print("{} dersinin vize notu:{},final notu{},yilsonu ortalamasi:{},sonuc:{}".format(ders2,drs2vize,drs2final,drs2ysnotu,sonuc2))
if drs3ysnotu>=50:
    sonuc3="GECTI"
else:
    sonuc3="KALDI"
print("{} dersinin vize notu:{},final notu{},yilsonu ortalamasi:{},sonuc:{}".format(ders3,drs3vize,drs3final,drs3ysnotu,sonuc3))
if drs4ysnotu>=50:
    sonuc4="GECTI"
else:
    sonuc4="KALDI"
print("{} dersinin vize notu:{},final notu{},yilsonu ortalamasi:{},sonuc:{}".format(ders4,drs4vize,drs4final,drs4ysnotu,sonuc4))

cevap2

sayilar = [42, 29, 17, 15, 10, 9, 6, 4, 2, 1]
toplam=0
for i in sayilar:
    toplam+=i
adet=len(sayilar)
ortalama=toplam/adet
for i in sayilar:
    if ortalama<i:
      sonuc="Yuksek"
    else:
      sonuc="Dusuk"
    print("sayi:",i,"ortalama:",ortalama,sonuc)

cevap3

#Verilen bir sayı aralığındaki tek sayıların toplamını hesaplayan bir Python programı yazın.
#Program, kullanıcıdan iki sayı isteyecek ve 
#bu iki sayı arasındaki tek sayıların toplamını hesaplayacaktır. 
#Program, kullanıcının geçersiz bir giriş yapması durumunda hata mesajı yazdıracaktır.
#Programi yazarken While dongusunu kullanmaniz gerekmektedir
giris=["a","b","c","d","e","f","g","h","j","k","l","m","n","o","p","r","s","t","u","v","w","y","z"]
while True:
    sayi1=input ("Aralik olusturmak  icin  Birinci sayiyi giriniz:")
    sayi2=input("Ikinci sayiyi giriniz:")
    
    if sayi1 in giris:
            print("Hatali giris yaptiniz!!!")
            pass
    elif sayi2 in giris:
            print("Hatali giris yaptiniz!!!")
            pass
    elif sayi1=="" or sayi2=="":
            print("Aralik bos gecilemez!!!") 
            pass
    else:
        sayi1=int(sayi1)
        sayi2=int(sayi2)
        toplam=0
        for x in range(sayi1,sayi2+1):
            if x%2==1:
                toplam+=x
        print("Araliktaki tek sayilarin toplami: ",toplam)       
