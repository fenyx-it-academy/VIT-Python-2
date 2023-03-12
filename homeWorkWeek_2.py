# Soru - 1

# kullanicidan input ile ilgili verileri alıyoruz.

ad = input("Adinizi giriniz: ")
soyad = input("Soyadinizi giriniz: ")
ogrenciNo = int(input("5 Haneli Ogrenci Numaranizi giriniz: "))

# ders isimleri alıyoruz.

ilkDers = input("Ilk Dersinizin Adini giriniz: ")
ikinciDers = input("Ikinci Dersinizin Adini giriniz: ")
ucuncuDers = input("Ucuncu Dersinizin Adini giriniz: ")
dorduncuDers = input("Dorduncu Dersinizin Adini giriniz: ")

# notlari aliyoruz

ilkDersVizeNotu = int(input("Ilk Dersinizin Vize Notu giriniz: "))
ilkDersFinalNotu = int(input("Ilk Dersinizin Final Notu giriniz: "))
ikinciDersVizeNotu = int(input("Ikinci Dersinizin Vize Notu giriniz: "))
ikinciDersFinalNotu = int(input("Ikinci Dersinizin Final Notu giriniz: "))
ucuncuDersVizeNotu = int(input("Ucuncu Dersinizin Vize Notu giriniz: "))
ucuncuDersFinalNotu = int(input("Ucuncu Dersinizin Final Notu giriniz: "))
dorduncuDersVizeNotu = int(input("Dorduncu Dersinizin Vize Notu giriniz: "))
dorduncuDersFinalNotu = int(input("Dorduncu Dersinizin Final Notu giriniz: "))

# vize final ortalamalari hesaplamalari yapiyoruz

ilkDersOrt = (ilkDersVizeNotu * 0.4) + (ilkDersFinalNotu * 0.6)
ikinciDersOrt = (ikinciDersVizeNotu * 0.4) + (ikinciDersFinalNotu * 0.6)
ucuncuDersOrt = (ucuncuDersVizeNotu * 0.4) + (ucuncuDersFinalNotu * 0.6)
dorduncuDersOrt = (dorduncuDersVizeNotu * 0.4) + (dorduncuDersFinalNotu * 0.6)

# ortalamalar sonucunda kaldi veya gecti yazdiriyoruz

if ilkDersOrt < 50:
    print("Sayin,", ogrenciNo, "Ogrenci Nolu,", ad, "",
          soyad, "", ilkDers, "dersinden 'KALDINIZ'".upper())
else:
    print("Sayin,", ogrenciNo, "Ogrenci Nolu,", ad, "",
          soyad, "", ilkDers, " dersinden 'GECTINIZ'".upper())
if ikinciDersOrt < 50:
    print("Sayin,", ogrenciNo, "Ogrenci Nolu,", ad, "",
          soyad, "", ikinciDers, " dersinden 'Kaldiniz'".upper())
else:
    print("Sayin,", ogrenciNo, "Ogrenci Nolu,", ad, "",
          soyad, "", ikinciDers, " dersinden 'GECTINIZ'".upper())
if ucuncuDersOrt < 50:
    print("Sayin,", ogrenciNo, "Ogrenci Nolu,", ad, "",
          soyad, "", ucuncuDers, " dersinden 'Kaldiniz'".upper())
else:
    print("Sayin,", ogrenciNo, "Ogrenci Nolu,", ad, "",
          soyad, "", ucuncuDers, " dersinden 'GECTINIZ'".upper())
if dorduncuDersOrt < 50:
    print("Sayin,", ogrenciNo, "Ogrenci Nolu,", ad, "",
          soyad, "", dorduncuDers, " dersinden 'Kaldiniz'".upper())
else:
    print("Sayin,", ogrenciNo, "Ogrenci Nolu,,", ad, "",
          soyad, "", dorduncuDers, " dersinden 'GECTINIZ'".upper())


#######################################################

# Soru - 2

sayilar = [42, 29, 17, 15, 10, 9, 6, 4, 2, 1]

# for ile listeyi donuyoruz ve i degerine atiyoruz. her i degerini de toplam degiskenine toplatiyoruz.
# uzunluk degiskenine len fonksiyonu ile listenin elema uzunlugunu atiyoruz
# liste uzunlugu ve liste eleman toplaminin ortalamasini bulabiliyoruz
toplam = 0
for i in sayilar:
    toplam += i
uzunluk = len(sayilar)
ort = toplam/uzunluk
print("Listedeki sayilarin ortalamasi:", ort)

# buldugumuz ortalama ile liste icindeki sayilarin dusuk mu yuksek mi oldugunu yine for ile listeyi dolasarak tespit edebiliriz.

dusuk = 0
yuksek = 0
# dusuk ve yuksek ile de if icindeki her yuksek ve dusuk tespit edilen durumu sirasiyla saydirarak toplatiyoruz
for i in sayilar:
    if ort > i:
        print("Listedeki Sayi:", i, ", Ortalama: ",
              ort, ", Ortalamadan Dusuk")
        dusuk += 1
    else:
        print("Listedeki Sayi:", i, ", Ortalama: ",
              ort, ", Ortalamadan Yuksek")
        yuksek += 1

print("Ortalamadan Dusuk olanlarin Sayisi:", dusuk,
      ", Ortalamadan Yuksek olanlarin Sayisi:", yuksek)


########################################################

# Soru - 3
# kullanicidan 2 sayi araligi almasini istiyoruz
sayi1 = int(input("Bir Sayi giriniz: "))
sayi2 = int(input("Ikinci Sayiyi giriniz: "))

# while true ile sonsuz dongu olusturuyoruz. donguden sonuc aldigimizda break ile cikmasini sagliyoruz
topla = 0
while True:

    for i in range(sayi1, sayi2):
        if (i % 2 == 1):
            topla += i
    break
if sayi1 > sayi2:
    print("Lutfen 1. sayiyi 2. sayidan kucuk giriniz")
else:
    print("Girdiginiz sayilar arasindaki tek sayilarin toplami:", topla)
