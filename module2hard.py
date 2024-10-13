import random

n = random.randrange(3, 21)
result = []

for i in range(1, n):
    for j in range(i, n):
        pair_sum = i + j
        if n % pair_sum == 0 and i != j:
            result += str(i) + str(j)

print(f'Число в первой табличке: {n}')
print(f'Пароль: {(result)}')

