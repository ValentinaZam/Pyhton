# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, 
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

# n = input("Введите числа через пробел:  ").split()
# print(n)

#1 3 8 5 6 1 9 4 10   =  1 

with open('spisok.txt', 'r') as n:
    list = n.read()
    print(list)
    list = list.split()
# if list[i] - 1 != list[i - 1]
for i in range(2, len(list)):
    #if list[i] - 1 != list[i - 1]
    if int(list[i]) - 1 == int(list[i - 1]):
        continue
    else:
        print(int(list[i]) - 1)



