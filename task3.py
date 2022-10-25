# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.

import random

numbers = [random.randint(0, 10) for i in range(10)]
print(numbers)

result = []
dubl = []

duplicatedCount = 0
result.append(numbers[0])

for i in numbers[1:]:
    if i in result:
        if not i in dubl:
            dubl.append(i)    
        continue
    result.append(i)

print(result)
print(dubl)
print(len(dubl))