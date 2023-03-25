#Soru-1 : Kullanıcıdan Adi, Soyadi, Ogrenci Numarasi, 4 ders adi, bu derslerin Vize ve Final notlari istenecektir. 
# Vize notunun % 40′ı ile Final Notunun %60′ınin toplamı yil sonu ortalamasini verecektir. 
#Ortalama 50‘den küçükse ekranda “KALDI“, 50 ve üstüyse ekranda “GEÇTİ” yazdırılacaktır. 
# Bu yazdirma islemi 4 ders icinde yapilacak ve dersler alt alta yazdirilacaktir.

ad=input("Adini gir:          ")
soyad=input("Soyadini gir:       ")
no=int(input("Numarani gir:       "))
print("******************************")
ders=["matematik","fizik","kimya","edebiyat"]
matv=int(input("matematik vize notunu girin  :       "))
edev=int(input("edebiyat vize notunu girin   :       "))
fizv=int(input("fizik vize notunu girin      :       "))
kimv=int(input("kimya vize notunu girin      :       "))
print("******************************")
matf=int(input("matematik final notunu girin  :      "))
edef=int(input("edebiyat final notunu girin   :      "))
fizf=int(input("fizik final notunu girin      :      "))
kimf=int(input("kimya final notunu girin      :      "))
print("------------------------------------------------")
mat_ort=(matv*40/100)+(matf*60/100)
ede_ort=(edev*40/100)+(edef*60/100)
fiz_ort=(fizv*40/100)+(fizf*60/100)
kim_ort=(kimv*40/100)+(kimf*60/100)
print("-------------------------------------------------")
if mat_ort<50:
    print("matematik ortalaman= " + str( mat_ort) + " KALDIN ")
else:
    print("matematik ortalaman= " + str( mat_ort) + " GECTIN ")
if ede_ort<50:
     
    print("edebiyat ortalaman=  " + str(ede_ort) + " KALDIN ")
else:
    print("edebiyat ortalaman=  " + str(ede_ort) + " GECTIN ")
    
          
if fiz_ort <50:
    print("fizik ortalaman=     " + str(fiz_ort) + " KALDIN ")
else:
    print("fizik ortalaman=     " + str(fiz_ort) + " GECTIN ")
     
if kim_ort <50:

     
    print("kimya ortalaman=     " + str(kim_ort) + " KALDIN ")
else:
    print("kimya ortalaman=     " + str(kim_ort) + " GECTIN ") 
    
    
       
#Soru-2 : Aşağıdaki listede bulunan sayıların ortalamasını hesaplayan bir Python programı yazın. 
# Daha sonra, listedeki her bir sayıyı, ortalamadan büyük olanlar "yuksek", 
# ortalamadan küçük olanlar "dusuk" olarak ayıran bir "for" 
# döngüsü ekleyin ve her bir grubun sayısını ekrana yazdırın.
#sayilar = [42, 29, 17, 15, 10, 9, 6, 4, 2, 1]
sayilar = [42, 29, 17, 15, 10, 9, 6, 4, 2, 1]
toplam = 0
for i in sayilar:
    toplam += i
ortalama = toplam / len(sayilar)
print("sayilarin ortalamasi= " , ortalama)
yuksek = 0
dusuk = 0
for i in sayilar:
    if i > ortalama:
        print(i,"YUKSEK")
        yuksek += 1
    elif i < ortalama:
        print(i,"DUSUK")
        dusuk += 1
print(f"Yüksek: {yuksek}   Dusuk: {dusuk}")

#Soru-3: Verilen bir sayı aralığındaki tek sayıların toplamını hesaplayan 
# bir Python programı yazın. Program, kullanıcıdan iki sayı isteyecek 
# ve bu iki sayı arasındaki tek sayıların toplamını hesaplayacaktır.
# Program, kullanıcının geçersiz bir giriş yapması durumunda 
# hata mesajı yazdıracaktır.
# Programi yazarken While dongusunu kullanmaniz gerekmektedir.


kontrol=True
while kontrol:
    try:
        a = int(input("Lutfen bir sayi girin :          "))
        b = int(input("Lutfen bir sayi daha girin :     "))
        kontrol=False
    except:
        print("Lütfen sadece sayı girişi yapınız..")
    
        kontrol=True

liste = range(a,b) 
i = 0
toplam = 0
  
# while döngüsü
while(i < len(liste)): 

      
    # tek sayı kontrolü 
    if liste[i] % 2 != 0:
        toplam += liste[i]
                
    i += 1
print("toplam", toplam)


   
    




