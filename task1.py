# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.

import random

numbers = [random.randint(0, 10) for i in range(10)]
print(numbers)

result = lambda x: x > 5
result = list(filter(result, numbers))
print(result)