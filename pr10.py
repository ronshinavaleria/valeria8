# Чтение данных из файла
with open('Роньшина_Валерия_Игоревна_УБ-51_vvod.txt', 'r') as file:
    # Читаем первую строку - длина массива
    b = int(file.readline().strip())
    # Читаем остальные строки - элементы массива
    a = []
    for c in range(b):
        line = file.readline().strip()
        a.append(int(line))
# Обработка данных (остается без изменений)
sm = 0
pr = 1
for i in range(0, len(a)):
    sm += a[i]
    pr *= a[i]
# Запись результатов в файл
with open('Роньшина_Валерия_Игоревна_УБ-51_vivod.txt', 'w') as file:
    file.write(f'Массив: {a}\n')
    file.write(f'Сумма элементов: {sm}\n')
    file.write(f'Произведение элементов: {pr}\n')
print("Результаты записаны в файл")

import os
# Автоматическое создание входного файла если он не существует
input_filename = 'Роньшина_Валерия_Игоревна_УБ-51_vvod.txt'
if not os.path.exists(input_filename):
    with open(input_filename, 'w') as f:
        f.write('6\n')    # Длина массива
        f.write('10\n')   # Элемент 1
        f.write('0\n')    
        f.write('20\n')   
        f.write('0\n')    
        f.write('30\n')   
        f.write('40\n')   
    print(f"Создан файл {input_filename} с тестовыми данными")
# Чтение данных из файла
with open(input_filename, 'r') as file:
    # Читаем первую строку - длина массива
    b = int(file.readline().strip())
    # Читаем остальные строки - элементы массива
    a = []
    for c in range(b):
        line = file.readline().strip()
        a.append(int(line))
# Обработка данных (остается без изменений)
sarf = 0
sm = 0
for i in range(0, len(a)):
    sm += a[i]
sarf = sm // b
# Заменяем нулевые элементы на среднее арифметическое
original_array = a.copy()  # Сохраняем исходный массив для вывода
for i in range(0, len(a)):
    if a[i] == 0:
        a[i] = sarf
# Запипь результатов в файл
output_filename = 'Роньшина_Валерия_Игоревна_УБ-51_vivod.txt'
with open(output_filename, 'w') as file:
    file.write('ИСХОДНЫЕ ДАННЫЕ:\n')
    file.write(f'Длина массива: {b}\n')
    file.write(f'Исходный массив: {original_array}\n\n')
    file.write('ВЫЧИСЛЕНИЯ:\n')
    file.write(f'Сумма элементов: {sm}\n')
    file.write(f'Среднее арифметическое: {sarf}\n\n')
    file.write('РЕЗУЛЬТАТ:\n')
    file.write(f'Измененный массив: {a}\n')
    file.write('(Все нулевые элементы заменены на среднее арифметическое)\n')
print(f"Результаты записаны в файл {output_filename}")
print(f"Исходный массив: {original_array}")
print(f"Измененный массив: {a}")
print(f"Среднее арифметическое: {sarf}")
