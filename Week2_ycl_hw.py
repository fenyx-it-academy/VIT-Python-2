#Soru-1 : Kullanıcıdan Adi, Soyadi, Ogrenci Numarasi, 4 ders adi, 
#bu derslerin Vize ve Final notlari istenecektir. 
#Vize notunun % 40′ı ile Final Notunun %60′ınin toplamı yil sonu ortalamasini verecektir. 
#Ortalama 50‘den küçükse ekranda “KALDI“, 50 ve üstüyse ekranda “GEÇTİ” yazdırılacaktır. 
#Bu yazdirma islemi 4 ders icinde yapilacak ve dersler alt alta yazdirilacaktir.


name=input("Ogrenci adini giriniz: ")
surname=input("Ogrenci soyadinizi giriniz: ")
number=input("Ogrenci numarasini giriniz: ")
les = 0
durum=""
while les < 4:
    name_les = input("dersin adini girin: ")
    vize = int(input("vize notunu girin: "))
    final = int(input("final notunu girin: "))
    medium = (vize*0.4) + (final*0.6)
    les+=1
    if medium >= 50:
        durum="GECTI"
        print('Ders:{}, Ortalama:{}, {}'.format(name_les,medium,durum))
    else:
        durum="KALDI"
        print('Ders:{}, Ortalama:{}, {}'.format(name_les,medium,durum))

#Soru-2 : Aşağıdaki listede bulunan sayıların ortalamasını hesaplayan bir 
#Python programı yazın. Daha sonra, listedeki her bir sayıyı, 
# ortalamadan büyük olanlar "yuksek", ortalamadan küçük olanlar "dusuk" olarak 
# ayıran bir "for" döngüsü ekleyin ve her bir grubun sayısını ekrana yazdırın.

sayilar = [42, 29, 17, 15, 10, 9, 6, 4, 2, 1]
toplam = 0
yuksek = 0
dusuk = 0
for i in sayilar:
    toplam +=i
ortalama = toplam / len(sayilar)    
for i in sayilar:
        if ortalama > i:
            yuksek +=1
        else :
            dusuk +=1     
        
print("""
      {} sayilar listesinin ortalamasidir. 
      {} kadar sayi ortalamadan buyuktur. 
      {} kadar ise kucuktur.""".format(ortalama, yuksek, dusuk))    


#Soru-3: Verilen bir sayı aralığındaki tek sayıların toplamını hesaplayan 
# bir Python programı yazın. Program, kullanıcıdan iki sayı isteyecek 
# ve bu iki sayı arasındaki tek sayıların toplamını hesaplayacaktır. 
# Program, kullanıcının geçersiz bir giriş yapması durumunda 
# hata mesajı yazdıracaktır.
# Programi yazarken While dongusunu kullanmaniz gerekmektedir.

sayi_min = int(input("Lutfen kucuk bir sayi giriniz: "))
sayi_max = int(input("Lutfen buyuk bir sayi giriniz: "))
tek_toplam=0
ilk_sayi=sayi_min+1

if sayi_max > sayi_min:
    
    while ilk_sayi < sayi_max:
    
        if (ilk_sayi % 2 == 1):
            tek_toplam+=ilk_sayi
        ilk_sayi+=1
  
    print(tek_toplam) 
           
else:
    print("Tekrar deneyin!!!")        
           

        
        




