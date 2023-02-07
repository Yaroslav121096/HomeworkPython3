# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def Random(args):
    import random
    for i in range(size):
        numbers.append(random.randint(1, 10))


size = int(input("Задайте размер списка: "))
numbers = []
Random(numbers)
print(f"Изначальный список:\n{numbers}")

n = len(numbers)//2 + 1 if len(numbers) % 2 != 0 else len(numbers)//2
newNumbers = [numbers[i]*numbers[len(numbers)-i-1] for i in range(n)]
print(f"Произведение пар чисел списка:\n{newNumbers}")
