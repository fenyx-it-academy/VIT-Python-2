#question1
name = input("Adınız nedir? ")
surname = input("Soyadınız nedir? ")
number = input("Öğrenci numarasınız nedir? ")

lessons = list()
exams = list()

for i in range(1,5):
    lessons.append(input(f"{i}.Dersi giriniz.. :"))
    
    vize = int(input(f"{i}. dersin vize notu :"))
    final = int(input(f"{i}. dersin final notu :"))

    exams.append(vize*0.40 + final*0.60)


for i in range(4):
    
    if (exams[i]) >= 50 :
        print(number, "numaralı öğrenci",name, surname,lessons[i],"dersinden", exams[i]," not ortalamasıyla GEÇTi..")

    else:
        print(number, "numaralı öğrenci",name, surname, lessons[i],"dersinden",exams[i]," ile dersten KALDI")


print("---------------------------------------------------------------------")


#question2
sayilar = [42, 29, 17, 15, 10, 9, 6, 4, 2, 1]

for i in sayilar:
    avg = sum(sayilar)/len(sayilar)

dusuk = [i for i in sayilar if i < avg]
yuksek = [i for i in sayilar if i >= avg]
print(avg)
print(f"Ortalaması 50'den düşük olan sayılar {dusuk}")
print(f"Ortalaması 50'den yüksek olan sayılar {yuksek}")

print("---------------------------------------------------------------------")

#question3
while True:

    num1 = input("1. sayıyı giriniz :")
    num2 = input("2. sayıyı giriniz :")

    if num1 > num2:
        print("1. sayı 2. sayıdan küçük olmalıdır. Tekrar deneyiniz.")
        continue
    
    tek = [i for i in range(int(num1)+1,int(num2)) if i % 2 == 1]

    print(tek)

    print(f"Listede ki tek sayıların toplamı {sum(tek)}.")




