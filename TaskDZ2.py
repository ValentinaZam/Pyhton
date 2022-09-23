# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

for x in 1, 0:
    for y in 1, 0:
        for z in 1, 0:
            if not(x or y or z) == (not x and not y and not z):
                print(f"Утверждение истинно")
            else:
                print(f"Утверждение ложно")
    
