# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное
# число N – количество элементов в массиве. В последующих  строках записаны 
# N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1


N = int(input('ВВЕДИТЕ НАТУРАЛЬНОЕ ЧИСЛО N: '))

array = list()
for i in range(1, N + 1):
    array.append(i)
print(array)

X = int(input('ВВЕДИТЕ НУЖНОЕ ЧИСЛО: '))
count = 0
if  X == N:
  count = count + 1
print("ВВЕДЁННОЕ НАМИ ЧИСЛО ВСТРЕЧАЕТСЯ В ДАННОМ СПИСКЕ" ,count,  "РАЗ")    


