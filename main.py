import random
import math
def disper():
    result = 0
    for i in list_elements:
        result += i - mat_ojidanie
    result = 1/(N - 1) * result
    print (result)
random.seed()
sum = 0
kol = 0
N = 100 # кол-во итераций
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
temp_sorted_list_element = sorted(list_elements)
for item in temp_sorted_list_element:
    if (item >= local_segment):
        local_segment += (b - a) / count_segemnts
        i += 1
    numbers1[i] += 1

variable = count_segemnts / N
ideal = N / count_segemnts

result = 0
for item in range(len(numbers1) - 1):
    result += numbers1[item] - ideal


print("Кол-во интервалов:")
print(count_segemnts)
print("Значение Хи-квадрат")
print(math.pow(result, 2) * variable)
print('Оценка мат ожидания для ' + str(N) + ' итераций')
mat_ojidanie = sum / N
print(mat_ojidanie)
print("Дисперсия")
disper()


