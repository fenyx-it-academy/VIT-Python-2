#Soru - 1
name= input("Your name: ")
last_name= input("Your last name: ")
school_number= input("Your School Number: ")
lesson_1 = input("1. Dersiniz: ")
lesson_2 = input("2. Dersiniz: ")
lesson_3 = input("3. Dersiniz: ")
lesson_4 = input("4. Dersiniz: ") 
vize_leson_1= int(input(f"{lesson_1} Vize Notu: "))
final_leson_1= int(input(f"{lesson_1} Final Notu: "))
vize_leson_2= int(input(f"{lesson_2} Vize Notu: "))
final_leson_2= int(input(f"{lesson_2} Final Notu: "))
vize_leson_3= int(input(f"{lesson_3} Vize Notu: "))
final_leson_3= int(input(f"{lesson_3} Final Notu: "))
vize_leson_4= int(input(f"{lesson_4} Vize Notu: "))
final_leson_4= int(input(f"{lesson_4} Final Notu: "))

ortalama_1 = vize_leson_1*0.40 + final_leson_1*0.60
ortalama_2 = vize_leson_2*0.40 + final_leson_2*0.60
ortalama_3 = vize_leson_3*0.40 + final_leson_3*0.60
ortalama_4 = vize_leson_4*0.40 + final_leson_4*0.60

print(f"Merhaba {name} {last_name} Girdiğiniz notlara göre karnenizi aşağıdadır:")
print(f"""
Ad: {name}
Soyad: {last_name}
Okul No: {school_number} 
""")

if ortalama_1<50:
    print(f"{lesson_1} --> KALDI")
else:
    print(f"{lesson_1} --> GEÇTİ")
if ortalama_2<50:
    print(f"{lesson_2} --> KALDI!")
else:
    print(f"{lesson_2} --> GEÇTİ")
if ortalama_3<50:
    print(f"{lesson_3} --> KALDI")
else:
    print(f"{lesson_3} --> GEÇTİ")
if ortalama_4<50:
    print(f"{lesson_4} --> KALDI")
else:
    print(f"{lesson_4} --> GEÇTİ")

# Soru-2
sayilar = [42, 29, 17, 15, 10, 9, 6, 4, 2, 1]

sum=0
for i in sayilar:
    sum += i
   
everage = sum/len(sayilar)
print(f"Listedeki sayıların ortalaması: {everage}")

for j in sayilar:
    if j > everage:
        print(f"{j} -> 'Yüksek'")
    elif j < everage:
        print(f"{j} ->  'Düşük'")    
    else:
        print(f"{j} ->  'Eşit'") 

#Soru-3
first_number = int(input("İlk Sayı: "))
second_number = int(input("İkinci Sayı: "))

sum = 0
if first_number%2==1:
    numbers= first_number
else:
    numbers=first_number+1


while first_number<second_number:
    sum +=numbers
    numbers+=2 
    if numbers > second_number:
        break

else:
    print("Hatalı Giriş Yaptınız!")
print(sum if sum>0 else "", end="")
    
