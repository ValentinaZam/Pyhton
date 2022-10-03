n = int(input('Введите число: '))
b = ''

while n > 0:
    b = str(n % 2) + b
    n //= 2

print(b)