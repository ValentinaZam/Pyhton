# 2. Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
from math import *
n = int(input("Введите положительное число N:  "))
if n < 1:
    print("Число у вас, сударь, отрицательное! А надо ПОЛОЖИТЕЛЬНОЕ!")
else:
    list = [factorial(i) for i in range(1, n + 1)] 
    print(list)