# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма 
# первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

"""num = int(input("Введите шестизначное число: "))
s1 = num[0] + num[1] + num[2]
s2 = num[3] + num[4] + num[5]
if s1 == s2:
  print("YES")
else:
  print("NO")"""
  
"""n = int(input())
d = list(map(int, list(f'{n:06}')))
print(('NO', 'YES')[sum(d[:3])==sum(d[3:])])"""

num = int(input("Введите номер билета :"))

a = num // 1000
b = num % 1000

d1 = a // 100
d2 = a % 100//10
d3 = a % 10

sum1 = d1 + d2 + d3
print("Сумма первых трех чисел--->",sum1)
d4 = b // 100
d5 = b % 100//10
d6 = b % 10

sum2 = d4 + d5 + d6
print ("Сумма последних трех чисел--->",sum2)
if sum1 == sum2:
  print("YES, ВЫИГРЫШ")
else:
  print("NO, ПРОИГРЫШ")