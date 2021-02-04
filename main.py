import random
import math

random.seed()
sum = 0
kol = 0
N = 10000  # кол-во итераций
a = 1  # начало интервала
b = 100  # конец интервала
count_segemnts = round(1 + 3.22 * math.log(N))  # кол-во отрезков
list_elements = list()
for i in range(N):
    num1 = random.randint(a, b)  # Случайное число от 0 до 1
    list_elements.append(num1)
    sum += num1
    # print(num1)

local_segment = count_segemnts
numbers1 = []
for i in range(count_segemnts):
    numbers1.append(0)
i = 0
for item in sorted(list_elements):
    if (item >= local_segment):
        local_segment += count_segemnts
        i += 1
    numbers1[i] += 1

result = 0
# дисперсию надо
variable = N / count_segemnts
for item in numbers1:
    result += (item - variable) * (item - variable)
print("Кол-во интервалов:")
print(count_segemnts)
print("Значение Хи-квадрат")
print(result*count_segemnts/N)
print('Оценка мат ожидания для ' + str(N) + ' итераций')
print(sum / N)
