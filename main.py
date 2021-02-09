import random
import math
import json

random.seed()


def read_settings():
    with open('settings.json', 'r', encoding='utf-8') as f:  # открыли файл с данными
        settings = json.load(f)
        return settings


settings = read_settings()
print()

sum = 0
kol = 0
N = settings['N']  # кол-во итераций
a = settings['a']  # начало интервала(всегда 0)
b = settings['b']  # конец интервала()


def write_in_file():
    file = open("otus.txt", "w")
    file.write("Кол-во интервалов: ")
    file.write(str(count_segemnts))
    file.write("\nЗначение Хи-квадрат: ")
    file.write(str(math.pow(result, 2) * variable))
    file.write('\nОценка мат ожидания для ' + str(N) + ' итераций: ')
    mat_ojidanie = sum / N
    file.write(str(mat_ojidanie))
    file.write("\nДисперсия")
    file.write(str(disper()))
    file.close()


def disper():
    result = 0
    for i in list_elements:
        result += i - mat_ojidanie
    result = 1 / (N - 1) * result
    return result


# a+(b-a)*R
count_segemnts = math.ceil(1 + 3.22 * math.log(N))  # кол-во отрезков
list_elements = list()
for i in range(N):
    num1 = random.random() * (b-a)
    list_elements.append(num1)
    sum += num1

numbers1 = []
for i in range(count_segemnts):
    numbers1.append(0)
local_segment = (b - a) / count_segemnts
i = 0
temp_sorted_list_element = sorted(list_elements)
for item in temp_sorted_list_element:
    if item >= local_segment:
        local_segment += (b - a) / count_segemnts
        i += 1
    numbers1[i] += 1

variable = count_segemnts / N
ideal = N / count_segemnts

result = 0
for item in range(len(numbers1)):
    print('кол-во попаданий в ' + str(item) + ' интервале')
    print(numbers1[item])
    result += numbers1[item] - ideal - 1

print("Кол-во интервалов:")
print(count_segemnts)
print("Значение Хи-квадрат")
print(math.pow(result, 2) * variable)
print('Оценка мат ожидания для ' + str(N) + ' итераций')
mat_ojidanie = sum / N
print(mat_ojidanie)
print("Дисперсия")
print(disper())
write_in_file()
