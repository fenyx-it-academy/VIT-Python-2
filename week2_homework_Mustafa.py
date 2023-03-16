VIT-Python-2
=====================================================================

# Soru-1 : Kullanıcıdan Adi, Soyadi, Ogrenci Numarasi, 4 ders adi, bu derslerin Vize ve Final notlari istenecektir.
# Vize notunun % 40′ı ile Final Notunun %60′ınin toplamı yil sonu ortalamasini verecektir.
# Ortalama 50‘den küçükse ekranda “KALDI“, 50 ve üstüyse ekranda “GEÇTİ” yazdırılacaktır.
# Bu yazdirma islemi 4 ders icinde yapilacak ve dersler alt alta yazdirilacaktir.

ad=str(input("Ad:"))
soyad=str(input("soyad:"))
ogrNo=str(input("Ogrenci Numarasi:"))

dersler=[]

yilsonu_notlari=[]

for i in range(4):
    ders=str(input(f"{i+1}. dersin adini giriniz:"))
    dersler.append(ders)
    
    vize=float(input(f"{i+1}. dersin vize notunu giriniz:"))
    finalnotu=float(input(f"{i+1}. dersin final notunu giriniz:"))
 
    yilsonu_notu=(vize*0.4) + (finalnotu*0.6)
    yilsonu_notlari.append(yilsonu_notu)
    
print(ad, soyad, "No:", ogrNo)

for i in range(4):
    if yilsonu_notlari[i]<50:
        print(f"{dersler[i]} dersi yilsonu notu:{yilsonu_notlari[i]} Sonuc: Kaldi")
    elif 100>=yilsonu_notlari[i]>=50:
        print(f"{dersler[i]} dersi yilsonu notu:{yilsonu_notlari[i]} Sonuc: Gecti")
    else:
         print(f"{dersler[i]} dersi icin hatali giris yaptiniz. Sonuc: Hesaplanamadi.")
        
    
    
    
=====================================================================

# Soru-2 : Aşağıdaki listede bulunan sayıların ortalamasını hesaplayan bir Python programı yazın.
# Daha sonra, listedeki her bir sayıyı, 
# ortalamadan büyük olanlar "yuksek", ortalamadan küçük olanlar "dusuk" olarak ayıran bir "for" döngüsü ekleyin
# ve her bir grubun sayısını ekrana yazdırın.

sayilar = [42, 29, 17, 15, 10, 9, 6, 4, 2, 1]
toplam=0
dusuk=[]
yuksek=[]

for i in range(len(sayilar)):
    toplam=toplam+sayilar[i]
    

s_ort=toplam/len(sayilar)

for i in range(len(sayilar)):
    if sayilar[i]<s_ort:
        dusuk.append(sayilar[i])
    elif sayilar[i]>s_ort:
        yuksek.append(sayilar[i])
    else:
        print("Ortalamaya esit")
print("Ortalama:", s_ort)
print(len(dusuk), " tane eleman ortalamadan dusuk. Bunlar:", dusuk)
print(len(yuksek), " tane eleman ortalamadan dusuk. Bunlar:", yuksek)

=====================================================================

# Soru-3: Verilen bir sayı aralığındaki tek sayıların toplamını hesaplayan bir Python programı yazın. 
# Program, kullanıcıdan iki sayı isteyecek ve bu iki sayı arasındaki tek sayıların toplamını hesaplayacaktır. 
# Program, kullanıcının geçersiz bir giriş yapması durumunda hata mesajı yazdıracaktır.
# Programi yazarken While dongusunu kullanmaniz gerekmektedir.

ilk=int(input("Ilk sayiyi giriniz:"))
son=int(input("Son sayiyi giriniz:"))

tekToplam=0
if ilk <=son:
    
    while ilk<=son:
        ilk+=1 
        if (ilk-1)%2!=0:
            tekToplam=tekToplam+ilk-1
           
    print(tekToplam)
    
else:
    print("Hatali giris")
=====================================================================
