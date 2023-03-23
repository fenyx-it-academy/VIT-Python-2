cevap1
#Kullanıcıdan Adi, Soyadi, Ogrenci Numarasi, 4 ders adi, bu derslerin Vize ve Final notlari istenecektir.
# Vize notunun % 40′ı ile Final Notunun %60′ınin toplamı yil sonu ortalamasini verecektir. 
# Ortalama 50‘den küçükse ekranda “KALDI“, 50 ve üstüyse ekranda “GEÇTİ” yazdırılacaktır.
# Bu yazdirma islemi 4 ders icinde yapilacak ve dersler alt alta yazdirilacaktir.
kullaniciadi=input("Adinizi giriniz:")
soyad=input("Soyadinizi giriniz:")
ogrencino=input("Ogrenci numaranizi giriniz:")
derss=1
toplam=""

while derss<5:
    ders=input("{} Dersinizi giriniz:".format(derss)).upper()
    dersvize=int(input("{} Dersinin vize notunu giriniz:".format(ders)))
    dersfinal=int(input("{} Dersinin final notunu giriniz:".format(ders)))
    dersyilsonu=(dersvize*0.4)+(dersfinal*0.6)
    
    if dersyilsonu>=50:
        sonuc="Gecti"
    else:
        sonuc="Kaldi"
    durum=("{} Dersinin vize notu:{},Final notu:{},yilsonu notu: {},Sonuc :{}\n".format(ders,dersvize,dersfinal,dersyilsonu,sonuc))
    derss+=1
    toplam+=durum

print("\n",kullaniciadi,soyad,ogrencino,"nolu ogrencinin notlari""\n")
    
print(toplam) 

2cevap

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

3 cevap
#Verilen bir sayı aralığındaki tek sayıların toplamını hesaplayan bir Python programı yazın.
#Program, kullanıcıdan iki sayı isteyecek ve 
#bu iki sayı arasındaki tek sayıların toplamını hesaplayacaktır. 
#Program, kullanıcının geçersiz bir giriş yapması durumunda hata mesajı yazdıracaktır.
#Programi yazarken While dongusunu kullanmaniz gerekmektedir
giris=["a","b","c","d","e","f","g","h","j","k","l","m","n","o","p","r","s","t","u","v","w","y","z"]
while True:
    sayi1=input ("Aralik olusturmak  icin  Birinci sayiyi giriniz:").lower()
    sayi2=input("Ikinci sayiyi giriniz:").lower()
    
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
