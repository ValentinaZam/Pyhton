# Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.
# [''ffff'.'3rfhg','4'] -> YES

from enum import Flag


num = ['ffff','3rfhg','4','52']
print(num)
flag = False
for i in num:
    if i.isdigit():
        flag = True
if flag:

    print("YES")
else:
    print("NO")
