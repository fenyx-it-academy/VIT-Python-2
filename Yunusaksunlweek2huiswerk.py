# Soru-1 : Kullanıcıdan Adi, Soyadi, Ogrenci Numarasi, 4 ders adi, 
# bu derslerin Vize ve Final notlari istenecektir. 
# Vize notunun % 40′ı ile Final Notunun %60′ınin toplamı yil sonu ortalamasini verecektir. 
# Ortalama 50‘den küçükse ekranda “KALDI“, 50 ve üstüyse ekranda “GEÇTİ” yazdırılacaktır. 
# Bu yazdirma islemi 4 ders icinde yapilacak ve dersler alt alta yazdirilacaktir.


ad = input("Lutfen adinizi giriniz :")
soyad = input("Lutfen soyadinizi giriniz :")
ogr_nu = input("Lutfen numaranizi giriniz :")


notlar = []
dersler = []
for i in range(4):
    ders = input("Dersin adini giriniz :")
    dersler.append(ders)
    
    vize = float(input(f"{dersler[i]}. nin Vize Notunuzu Girin : ")) # float(input("Vize notu :"))
    final = float(input(f"{dersler[i]}. nin Final Notunuzu Girin : "))
    ortalama = ((vize * 0.4) + (final * 0.6)) 
    notlar.append(ortalama) #ortalama bize daha sonra lazim oldugu icin notlar klasorunde sakliyoruz    

sonuc= []
for i in notlar:
    if i >=50:
        durum = "GECTI"
        sonuc.append(durum)
    
    else:
        durum = "KALDI"
        sonuc.append(durum)

for i in range(len(dersler)):
    print(dersler[i], " :", "Ortalama :", notlar[i], sonuc[i])
    

    
# Soru-2 : Aşağıdaki listede bulunan sayıların ortalamasını hesaplayan bir Python programı yazın. 
# Daha sonra listedeki her bir sayıyı, ortalamadan büyük olanlar "yuksek", 
# ortalamadan küçük olanlar "dusuk" olarak ayıran bir "for" döngüsü ekleyin ve her bir grubun sayısını ekrana yazdırın.

sayilar = [42, 29, 17, 15, 10, 9, 6, 4, 2, 1]

toplam = sum(sayilar)

print("Toplam :",toplam)

adet = len(sayilar)

ortalama = toplam / adet

print("Ortalama :", ortalama)

yukseklerin_sayisi= 0
dusuklerin_sayisi  = 0

yuksekler= []
dusukler =[]

for sayi in sayilar:

    if sayi > ortalama:
        yukseklerin_sayisi +=1
        yuksekler.append(sayi)
        
    else:
        dusuklerin_sayisi +=1 
        dusukler.append(sayi) #burada none uyarisi veriyor ve listenin sonuna ekleme yapmiyor o yuzden calistirmadim. hocaya sor?!!
        
print("Yuksek sayilarin adedi :", yukseklerin_sayisi, "Yuksek sayilar :", yuksekler)

print("Dusuk sayilarin adedi :", dusuklerin_sayisi, "Dusuk sayilar :", dusukler)    



# Soru-3: Verilen bir sayı aralığındaki tek sayıların toplamını hesaplayan bir Python programı yazın.
# Program, kullanıcıdan iki sayı isteyecek ve bu iki sayı arasındaki tek sayıların toplamını hesaplayacaktır.
# Program, kullanıcının geçersiz bir giriş yapması durumunda hata mesajı yazdıracaktır.
# Programi yazarken While dongusunu kullanmaniz gerekmektedir.

devam = True

while devam == True:
    
    sayi1 = int(input("Birinci sayiyi giriniz :"))

    sayi2 = int(input("Ikinci sayiyi giriniz :"))
    
    if sayi1 == sayi2:
        
        print("sayi1 ve sayi2 birbirine esit olamaz. Lutfen farkli bir sayi giriniz")
    
    else:
            
        toplam = 0

        for i in range(sayi1,sayi2):
            
            if i % 2 == 1:
                toplam += i
            
        print("Girdiginiz araliktaki tek sayilarin  toplami :", toplam)
        
        devam = False

