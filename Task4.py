# Напишите программу, которая будет на вход принимать число N
# и выводить числа от -N до N

# n = int(input())
# i = -n
# while i <= n:
#     print(i)
#     i+=1

#Второй вариант:
n = int(input())
mass = []
for i in range(-n,n+1,1):
    mass.append(i)
print(mass)
