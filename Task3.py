#Напишите программу, которая принимает на вход 
#5 чисел и находит максимальное из них.

c1 = int(input())
max = c1
for i in range(4):
    a = int(input())
    if a > max:
        max = a
print(max)

#Второй вариант:
# a = list(map(int,input().split()))
# maximum = max(a)
# print(maximum)