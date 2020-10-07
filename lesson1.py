# kvadrat_tomoni = float(input('kv:'))
# print("Kvadrat perimetri:", kvadrat_tomoni*4)
# print("Kvadrat Yuzasi:",kvadrat_tomoni**2)
# import math #import tashqi ichki kutubxonani kod qismiga yuklash
# a = float(input('a ni kiriting:'))#a ni haqiqiy son turida qabul qilib olish
# b = float(input("b o'zgaruvchini kiriting:"))#b ni haqiqiy son turida qabul qilib olish
# c = float(input('c :'))#c ni haqiqiy son turida qabul qilib olish
# pi = 3.14 # pi bu o'zgarmas son
# print("4burchak yuzasi:", a*b)
# print("4burchak perimetri:", 2*(a+b))
# print("Kubning hajmi:", a**3)
# print("Kub to'la sirti:", 6*(a**2))
# print("Aylana uzunligi:", pi*a)
# print("Parallelipepid hajmi:", a*b*c)
# print("Parallelipepid to'la sirti:", 2*((a*b)+(b*c)+(a*c)))
# print("O'rta geometrik:", round(math.sqrt(a*b),3)) # round sonlarni yaxlitlash
# print("Gipotenuza:", math.sqrt(a*a+b*b),
#  "\t\n 3 burchak perimetri:", a+b+math.sqrt(a*a+b*b))

# if a > b:
#     print('s1:', pi*a, 's2:', pi*b, 's3:', pi*(a-b))
# else:
#     print('R2 R1 dan katta')

# print("2 nuqta orasidagi masofa:", abs(b-a))

import math
x1 = float(input('x1:'))
x2 = float(input('x2:'))
y1 = float(input('y1:'))
y2 = float(input('y2:'))
print(math.sqrt(((x2-x1)**2)+((y2-y1)**2)))
