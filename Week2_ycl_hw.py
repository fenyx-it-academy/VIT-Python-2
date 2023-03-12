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






