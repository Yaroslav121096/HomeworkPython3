# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def Random(args):
    import random
    for i in range(size):
        numbers.append(round(random.random(), 2))


size = int(input("Задайте размер списка: "))
numbers = []
Random(numbers)
print(f"Изначальный список:\n{numbers}")

newNumbers = [round(i % 1, 2) for i in numbers if i % 1 != 0]
print(f"Разница между максимальным и миниммальным:\n{max(newNumbers) - min(newNumbers)}")