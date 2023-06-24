# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
l = int(input("Введите длину списка: "))
list_1 = []
i = 0
while len(list_1) <l:
    list_1.append(int(input("Введите число: ")))
    i+=1
print(list_1)
count =0
num = int(input("Введите искомое число: "))
if list_1[0]<=num:
    min_diff = num-list_1[0]
else:
    min_diff = list_1[0] - num
for j in range(len(list_1)):
    if ((list_1[j] - num) or (num-list_1[j]))<min_diff:
        min_num = list_1[j]
        if list_1[j]<=num:
            min_diff = num-list_1[j]
        else:
            min_diff = list_1[j] - num
print(min_num)
