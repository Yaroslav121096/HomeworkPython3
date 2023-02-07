# Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def Random(args):
    import random
    for i in range(size):
        numbers.append(random.randint(1, 10))


size = int(input("Задайте размер списка: "))
numbers = []
Random(numbers)
print(f"Изначальный список:\n{numbers}")

result = 0
for i in range(len(numbers)):
    if i % 2 != 0:
        result += numbers[i]

print(f"Сумма элементов, стоящих на нечётной позиции равна: {result}")
