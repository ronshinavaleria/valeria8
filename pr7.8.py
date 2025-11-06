def pr_chisla(num, vr=None):
    if vr is None:
        vr = num
    if vr == 0:
        return True
    cifra = vr % 10
    if cifra == 0 or num % cifra != 0:
        return False
    return pr_chisla(num, vr // 10)
n = int(input('Введите n: '))
result = []
for num in range(1, n + 1):
    if pr_chisla(num):
        result.append(num)
print(result)


def f(x):
    vrem = x[0]
    x[0]=x[len(x)-1]
    x[len(x)-1]=vrem
spisok = []
m = int(input('введите длину массива:'))
for i in range(m):
    print('введите', i+1, 'элемент массива')
    spisok.append(int(input()))
print(spisok)
f(spisok)
print(spisok)



