#Cevap 1

ad = input("Adiniz: ")
soy_ad = input("Soyadiniz: ")
dersler = ""
i = 0
while i < 4:
    ders_adi = input("Dersin Adi: ")
    vize = int(input("Vize Notu: "))
    final = int(input("Final Notu: "))
    ort = vize*0.4+final*0.6

    if ort < 50:

        sonuc = "KALDI"

    else:
        sonuc = "GECTI"
    a = f"{ders_adi} dersinden, {int(ort)} ortalama ile {sonuc}\n"
    dersler += a

    i += 1

print("\n" + ad, soy_ad, "\n")
print(dersler)


#Cevap 2

sayilar = [42, 29, 17, 15, 10, 9, 6, 4, 2, 1]
toplam = 0

for i in sayilar:
    toplam += i
ort = toplam/len(sayilar)

dusuk = []
yuksek = []

for i in sayilar:
    if i > ort:
        yuksek.append(i)
    else:
        dusuk.append(i)

print(f"{ort} ortalamasindan dusuk sayilar: {sorted(dusuk)}")

print(f"{ort} ortalamasindan yuksek sayilar: {sorted(yuksek)}")


#Cevap3

while True:
    sayi1 = input("Baslangic sayisi: ")
    if sayi1.isdecimal() == False:
        print("HATALI GIRIS Tekrar dene")
        continue
    sayi1 = int(sayi1)

    sayi2 = input("Bitis sayisi: ")
    if sayi2.isdecimal() == False:
        print("HATALI GIRIS Tekrar dene")
        continue
    sayi2 = int(sayi2)

    break

tek_sayilar_toplami = 0

while sayi1 < sayi2:

    if sayi1 % 2 == 1:
        tek_sayilar_toplami += sayi1
    sayi1 += 1
print("Tek sayilarin toplami :", tek_sayilar_toplami)

