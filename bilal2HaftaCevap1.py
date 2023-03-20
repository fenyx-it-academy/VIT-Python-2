#Soru-1 : Kullanıcıdan Adi, Soyadi, Ogrenci Numarasi, 4 ders adi, 
# 
# (İstediğimiz kadar ders kaydedebilecek şekilde yapıldı.) 
# 
# bu derslerin Vize ve Final notlari istenecektir. 
# Vize notunun % 40′ı ile Final Notunun %60′ınin toplamı yil sonu ortalamasini verecektir.
# Ortalama 50‘den küçükse ekranda “KALDI“, 
# 50 ve üstüyse ekranda “GEÇTİ” yazdırılacaktır. 
# Bu yazdirma islemi 4 ders icinde yapilacak ve dersler alt alta yazdirilacaktir.
adi=[]
soyadi=[]
numarasi=[]
dersAdi=[]
vize=[]
final=[]
while True:
    dersAdiStr=input("Ders isimlerini giriniz...:(Bitti ise çıkış için Q)")
    if dersAdiStr in "Qq":
        break
    dersAdi.append(dersAdiStr)
while True:
    adiStr=input("Öğrencinin adını giriniz ...: Çıkış için Q")
    if adiStr in "Qq":
        break
    adi.append(adiStr)
    soyadi.append(input("Öğrencinin soyadını giriniz ...:"))
    numarasi.append(input("Öğrencinin numarasını giriniz ...:"))
    for x in dersAdi:
        vize.append(input("{} dersinin vizesini giriniz...: ".format(x)))
        final.append(input("{} dersinin finalini giriniz...: ".format(x)))
index=0
dI=0
for ad in adi:
    print("{} {} {}".format(ad,soyadi[index],numarasi[index]))
    for x in dersAdi:
        ortalama=int(float(vize[dI])*0.4+float(final[dI])*0.6)
        if ortalama<50:
            sonuc="Kaldı"
        else:
            sonuc="Geçti"
        print("{} dersi Vize {}, Final {}, Ortalama  {}, Sonuç: {}".format(x,vize[dI],final[dI],ortalama,sonuc))
        dI+=1
    index+=1
