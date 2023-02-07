# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

def Random(args):
    import random
    for i in range(size):
        numbers.append(random.randint(1, 10))


size = int(input("Задайте размер списка: "))
numbers = []
x = int(input("Введите число для поиска: "))
Random(numbers)
print(f"Изначальный список:\n{numbers}")

distanses = {abs(x - num): num for num in numbers}
minDist = min(distanses)
nearestNumbers = distanses[minDist]
print(f"Число {nearestNumbers} является близжайшими к числу {x} числами списка и находятся на расстоянии {minDist}")