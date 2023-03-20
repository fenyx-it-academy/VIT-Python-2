#Soru-3: Verilen bir sayı aralığındaki tek sayıların toplamını hesaplayan 
# bir Python programı yazın. Program, kullanıcıdan iki sayı isteyecek 
# ve bu iki sayı arasındaki tek sayıların toplamını hesaplayacaktır.
# Program, kullanıcının geçersiz bir giriş yapması durumunda 
# hata mesajı yazdıracaktır.
# Programi yazarken While dongusunu kullanmaniz gerekmektedir.
sayilar=[]
index=0
hata=False
while True:
    hata=False
    sayi=input("Lütfen {}. sayıyı giriniz..: (Çıkış için Q)".format(index+1))
    if sayi in "Qq":
        break
    for x in sayi:
        if x in "0123456789":
            pass
        else:
            print("Lütfen sadece sayı girişi yapınız...")
            hata=True
            break
    if hata==False:
        sayilar.append(int(sayi))
        if index==1:
            break
        index+=1
tekSayiToplami=0
x=sayilar[0]
while x<=sayilar[1]:
#for x in range( sayilar[0],sayilar[1]+1):
    if x%2==1:
        tekSayiToplami+=x
    x+=1
print("{} ile {} arasındaki tek sayıların toplamı = {}".format(sayilar[0],sayilar[1],tekSayiToplami))
        
