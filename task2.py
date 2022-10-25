# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, описывающие возрастающую последовательность. Порядок элементов менять нельзя.

import random

numbers = [random.randint(0, 10) for i in range(10)]
print(numbers)

sub = []
sub.append(numbers[0])

for i in range(len(numbers)):
    if sub[-1] < numbers[i]:
        sub.append(numbers[i])

print(sub)
