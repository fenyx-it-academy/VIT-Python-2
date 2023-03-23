#Soru-1 : Kullanıcıdan Adi, Soyadi, Ogrenci Numarasi, 4 ders adi, bu derslerin Vize ve Final notlari istenecektir.
# Vize notunun % 40′ı ile Final Notunun %60′ınin toplamı yil sonu ortalamasini verecektir. 
#Ortalama 50‘den küçükse ekranda “KALDI“, 50 ve üstüyse ekranda “GEÇTİ” yazdırılacaktır.
# Bu yazdirma islemi 4 ders icinde yapilacak ve dersler alt alta yazdirilacaktir.
name = input("Adinizi yaziniz  :")
surname =input("Soyadinizi yaziniz  :")
nummer = int(input("Ogrenci numaranizi yaziniz  :"))

lesson1=input("Ders adini yaziniz : ")
print(" {} vize notunu asagi yaziniz ".format(lesson1),"\n","Sinava girmediyseniz ders notunu '0' yaziniz")
v_note1 =int(input(" vize notu yaziniz  :"))
print(" {} Final notunu asagi yaziniz".format(lesson1),"\n","Sinava girmediyseniz ders notunu '0' yaziniz")
f_note1 =int(input(" Final notu yaziniz  :"))
lesson1_average = float(v_note1)*0.4 + float(f_note1)* 0.6
if lesson1_average > 50 :
    sonuc1="GECTI"
else:
    sonuc1="KALDI"


lesson2 = input("Ders adini yaziniz  : ")
print(" {} vize notunu asagi yaziniz".format(lesson2),"\n","Sinava girmediyseniz ders notunu '0' yaziniz")
v_note2 =int(input(" vize notu yaziniz  :"))
print(" {} Final notunu asagi yaziniz".format(lesson2),"\n","Sinava girmediyseniz ders notunu '0' yaziniz")
f_note2 =int(input(" Final notu yaziniz  :"))
lesson2_average = float(v_note2)*0.4 + float(f_note2)* 0.6
if lesson2_average > 50 :
    sonuc2="GECTI"
else:
    sonuc2="KALDI"

lesson3=input("Ders adini yaziniz  :")
print(" {} vize notunu asagi yaziniz".format(lesson3),"\n","Sinava girmediyseniz ders notunu '0' yaziniz")
v_note3 =int(input("vize notu yaziniz :"))
print(" {} Final notunu asagi yaziniz".format(lesson3),"\n","Sinava girmediyseniz ders notunu '0' yaziniz")
f_note3 =int(input(" Final notu yaziniz  :"))
lesson3_average = float(v_note3)*0.4 + float(f_note3)* 0.6
if lesson3_average > 50 :
    sonuc3="GECTI"
else:
    sonuc3="KALDI"

lesson4=input("Ders adini yaziniz  :")
print(" {} vize notunu asagi yaziniz".format(lesson4),"\n","Sinava girmediyseniz ders notunu '0' yaziniz")
v_note4 =int(input("vize notu yaziniz  :"))
print(" {} Final notunu asagi yaziniz".format(lesson4),"\n","Sinava girmediyseniz ders notunu '0' yaziniz")
f_note4 =int(input(" Final notu yaziniz  :"))
lesson4_average = float(v_note4)*0.4 + float(f_note4)* 0.6
if lesson4_average > 50 :
    sonuc4="GECTI"
else:
    sonuc4="KALDI"
print("{} nolu ogrenci: Sayin {} {} ".format(nummer,name,surname))    
print("{} dersinden".format(lesson1), "{} ortalama ile ".format(int(lesson1_average)), sonuc1)
print("{} dersinden".format(lesson2), "{} ortalama ile ".format(int(lesson2_average)), sonuc2)
print("{} dersinden".format(lesson3), "{} ortalama ile ".format(int(lesson3_average)), sonuc3)
print("{} dersinden".format(lesson4), "{} ortalama ile ".format(int(lesson4_average)), sonuc4)



# Soru-2 : Aşağıdaki listede bulunan sayıların ortalamasını hesaplayan bir Python programı yazın.
# Daha sonra, listedeki her bir sayıyı, ortalamadan büyük olanlar "yuksek", 
#ortalamadan küçük olanlar "dusuk" olarak ayıran bir "for" döngüsü ekleyin ve her bir grubun sayısını ekrana yazdırın.

sayilar = [42, 29, 17, 15, 10, 9, 6, 4, 2, 1]
ort=sum(sayilar)/ len(sayilar)
print("Sayilarin ortalamasi  :", ort)
for i in sayilar :
    if i > ort :
        print("{} sayisi {}  ortalamasindan yuksektir".format(i,ort))
    else:
        print("{} sayisi {}  ortalamasindan dusuktur".format(i,ort))
        
        
#Soru-3: Verilen bir sayı aralığındaki tek sayıların toplamını hesaplayan bir Python programı yazın. 
#Program, kullanıcıdan iki sayı isteyecek ve bu iki sayı arasındaki tek sayıların toplamını hesaplayacaktır. 
#Program, kullanıcının geçersiz bir giriş yapması durumunda hata mesajı yazdıracaktır.
#Programi yazarken While dongusunu kullanmaniz gerekmektedir.
while True :
    print("ORNEK SAYILAR \" sayi1 = 5 ve sayi2 = 10 \" ")
    nummer1 = int(input("Bir sayi  yaziniz  :"))
    nummer2 = int(input("Bir sayi  yaziniz  :"))
    if nummer1 == nummer2 or nummer1<0 or nummer2<0 :
        print("Gecersiz sayi veya sayilar girdiniz")
    else:
        print("Islem devam ediyor")
        break
nummers =[nummer1,nummer2]
print(nummers)
topla=0
for i in range(nummer1,nummer2):
    if i%2==1 :
        topla+=i
print("{} ve {} arasindaki tek sayilar tolami : {}".format(nummer1,nummer2,topla))        
         
