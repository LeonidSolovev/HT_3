# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X

l = int(input("Введите длину списка: "))
list_1 = []
i = 0
while len(list_1) <l:
    list_1.append(int(input("Введите число: ")))
    i+=1
print(list_1)
count =0
num = int(input("Введите искомое число: "))
for j in range(len(list_1)):
    if num==list_1[j]:
        count +=1
print(count)
