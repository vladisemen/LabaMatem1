import random
import math
# дисперсию надо
random.seed()
sum = 0
kol = 0
N = 10  # кол-во итераций
a = 0  # начало интервала
b = 100  # конец интервала
count_segemnts = math.ceil(1 + 3.22 * math.log(N))  # кол-во отрезков
list_elements = list()
for i in range(N):
    num1 = random.randint(a, b)  # Случайное число от a До b
    list_elements.append(num1)
    sum += num1

local_segment = count_segemnts
numbers1 = []
for i in range(count_segemnts):
    numbers1.append(0)

i = 0
for item in sorted(list_elements):
    if (item >= local_segment):
        local_segment += (b - a) / count_segemnts
        i += 1
    numbers1[i] += 1
result = 0
variable = count_segemnts / N
ideal = N/count_segemnts
for item in numbers1:
    result += item - ideal
print("Кол-во интервалов:")
print(count_segemnts)
print("Значение Хи-квадрат")
print(math.pow(result, 2) *variable)
print('Оценка мат ожидания для ' + str(N) + ' итераций')
print(sum / N)
