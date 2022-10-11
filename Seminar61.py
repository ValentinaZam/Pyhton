# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

expression = str(input('Введите арифметического выражения: '))
result = eval(expression)
print(f'{expression} = {result}')

# import sympy
# list = input('Введите пример: ')
# print(list)
# result = 0
# if list.find('+') != -1:
#     list = list.split("+")   # 2+3*9
#     result = int(list[0]) + int(list[1])
# elif list.find('-') != -1:
#     list = list.split("-")   # 2+3*9
#     result = int(list[0]) - int(list[1])
# print(result)



    

