# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

def Random(args):
    import random
    for i in range(size):
        numbers.append(random.randint(1, 10))


size = int(input("Задайте размер списка: "))
numbers = []
Random(numbers)
x = int(input("Введите число X: "))
print(f"Изначальный список:\n{numbers}")
print(f"Число {x} встречается в списке {numbers.count(x)} раз(а)")