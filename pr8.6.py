m = int(input('Введите размер матрицы: '))
a = []
for i in range(m):
    b = []
    for j in range(m):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    a.append(b)
print('Исходная матрица:')
for i in range(m):
    for j in range(m):
        print(a[i][j], end=' ')
    print()
print('Наибольшие элементы в строках:')
for i in range(m):
    max_element = a[i][0]
    for j in range(1, m):
        if a[i][j] > max_element:
            max_element = a[i][j]
    print('Строка', i, ':', max_element)
print('Наименьшие элементы в столбцах:')
for j in range(m):
    min_element = a[0][j]
    for i in range(1, m):
        if a[i][j] < min_element:
            min_element = a[i][j]
    print('Столбец', j, ':', min_element)



n = int(input('Введите размер матрицы (нечетное число): '))
a = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [', i, ',', j, '] элемент')
        b.append(float(input()))
    a.append(b)
print('Исходная матрица:')
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
max_element = a[0][0]
max_i, max_j = 0, 0
for i in range(n):
    if a[i][i] > max_element:
        max_element = a[i][i]
        max_i, max_j = i, i
    if a[i][n-1-i] > max_element:
        max_element = a[i][n-1-i]
        max_i, max_j = i, n-1-i
center = n // 2
center_element = a[center][center]
a[center][center] = max_element
a[max_i][max_j] = center_element
print('Измененная матрица:')
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
print('Наибольший элемент на диагоналях:', max_element)
print('Позиция наибольшего элемента: [', max_i, ',', max_j, ']')
print('Центральный элемент:', center_element)
