N = [1, 2, 3, 7, 10]
M = []
num = N[0]
M.append(num)
for i in N:
    if num < N[i]:
        M.append(N[i])
        num = N[i]

print(M)