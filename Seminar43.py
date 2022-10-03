# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 2) с помощью дополнительных библиотек Python

import sympy

a = int(input("Введите число А: "))
b = int(input("Введите число B: "))
c = int(input("Введите число C: "))

x = sympy.Symbol('x')
d = a * x**2 + b * x + c

ans = sympy.solve(d , x)
print(ans)
print(a, b ,c)
