# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import math


def whileCycle():
    i = 0
    print("whileCycle_result: ", end=' ')
    while i <= 10:
        print(i, end=' ')
        i = i + 1
        if i > 7:
            i = i + 2
    print(i)


def whileCycle2():
    i = 0
    count = ''
    while i < 5:
        count += '*'
        if i % 2 == 0:
            count += '**'
        if i > 2:
            count += '***'
        i = i + 1
    print('whileCycle2_result: ', len(count))


def sumOnIntterval(a, b):
    result = a
    while a < b:
        a += 1
        result += a
    print('sumOnInterval_result: ', result)


def sumTillZero():
    print('Function will sum input int till it not "0"')
    n = int(input('Enter the number: '))
    result = 0
    while n != 0:
        result += n
        n = int(input('Enter the number: '))
    print('sumTillZero_result: ', result)


def sumTillZero2():  # pretty solution
    print('***sumTillZero2***')
    s = 0
    i = 1
    while i:
        i = int(input())
        s += i
    print("sumTillZero2_result: ", s)


def slicePie():  # divide prize belong 2 teams
    print("***slicePie***")
    a = int(input("a: "))
    b = int(input("b: "))
    d = a
    while d % a or d % b:
        d += a
    print("slicePie_result: ", d)


def breakContinue():
    i = 0
    while i < 5:
        a, b = input().split()
        a = int(a)
        b = int(b)
        if (a == 0) and (b == 0):
            break
        if (a == 0) or (b == 0):
            continue
        print(a * b)
        i += 1


def breakContinue2():
    i = 0
    s = 0
    while i < 10:
        i = i + 1
        s = s + i
        if s > 15:
            break
        i = i + 1


def breakContinue3():
    n = int(input())
    while n <= 100:
        if n < 10:
            n = int(input())
            continue
        print(n)
        n = int(input())


def forRange():
    print('For i in range(10)')
    for i in range(3, 10, 2):
        print(i)


def printStars():
    n = int(input())
    for i in range(n):
        print(n * '*')


def multiplyTable():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print('\t', end='')
    for m in range(c, d + 1):
        print(m, end='\t')
    for i in range(a, b + 1):
        print('\n')
        print(i, end='\t')
        for j in range(c, d + 1):
            print(i * j, end='\t')


def multiplyTable2():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    for g in range(c, d + 1):
        print('\t' + str(g), end='')
    print(end='\n')
    for i in range(a, b + 1):
        print(str(i) + '\t', end='')
        for j in range(c, d + 1):
            print(str(i * j), end='\t')
        print(end='\n')


def sumOfOddBetween():
    a, b = (int(i) for i in input().split())
    s = 0
    if a % 2 == 0:
        a += 1
    for i in range(a, b + 1, 2):
        s += i
    print(s)


def avg3():
    a = int(input())
    b = int(input())
    s = 0
    k = 0
    for i in range(a, b + 1):
        if i % 3 == 0:
            k += 1
            s += i
    print(s)


def avg3_2():
    a = int(input())
    b = int(input())
    s = 0
    while a % 3 != 0:
        a += 1
    for i in range(a, b + 1, 3):
        s += i
    print(s)


def stringMethods():
    s = input().lower()
    t = s.count('c') + s.count('g')
    print(t / len(s) * 100)


def slicing():
    s = 'qwerty'
    s[1]  # w
    s[1:4]  # wer
    s[:4]  # qwer
    s[4:]  # ty
    s[-4:]  # erty
    s[1:-1]  # wert
    s[1:-1:2]  # wr от первого до предпоследнего с шагом 2
    s[::-1]  # ytrewq
    k = 'abcdefghijk'
    print(k[3:6], end=' ')
    print(k[:6], end=' ')
    print(k[3:], end=' ')
    print(k[::-1], end=' ')
    print(k[-3:], end=' ')
    print(k[:-6], end=' ')
    print(k[-1:-10:-2])


def polindrom():
    polindrom_string = input('Первая строка: \t')
    x = polindrom_string[:math.ceil((len(polindrom_string) - 1) / 2)]
    y = polindrom_string[:math.ceil(len(polindrom_string) / 2) - 1:-1]
    print(x, y)
    print("y" if x == y else "n")


def shortGenom():
    dna = input()  # считываем строку
    print(dna[0], end='')  # выводим первый символ
    cnt = 1  # счетчик символов на единице
    for i in range(0, len(dna) - 1):  # итератор проходит по всем индексам символов кроме предпоследнего
        if dna[i] == dna[i + 1]:  # сравниваем символ по текущему индексу со следующим
            cnt += 1  # если символы одинаковые, то увеличиваем счетчик
        else:
            print(cnt, end='')  # если разные, то выводим значение счетчика
            print(dna[i + 1], end='')  # выводим следующий символ
            cnt = 1  # счетчик текущего символа на единице
    print(cnt)  # в конце распечатываем значение счетчика последнего символа


def sumOfSplitList():
    l = [int(i) for i in input().split()]
    result = 0
    for i in l:
        result += i
    print(result)


def sumOfNeighbours():
    a = [1, 5, 8, 20, 60]
    # a = [int(i) for i in input().split()]
    n = len(a)
    if n == 1:
        print(a[0])
    else:
        for i in range(n - 1):
            print(a[i - 1] + a[i + 1], end=" ")
        print(a[n - 2] + a[0])


def showRepited():
    a, c = [str(i) for i in input().split()], []
    for i in a:
        if i not in c and a.count(i) > 1:
            c.append(i)
            print(i, end=' ')


def listKata():
    seq = [2, 5, 1, 1, 7, 2, 1, 0]
    print(sorted(set(seq), key=seq.index))


def listFiltering():
    a = [1, 2, 'a', 'b', 0]
    print([i for i in a if type(i) == int])
    # return b


def lovefunc():
    flower1 = 915
    flower2 = 618
    if (flower1 % 2 == 0 and flower2 % 2 == 1) or (flower1 % 2 == 1 and flower2 % 2 == 0):
        print('True')
    else:
        print('False')
    # return (flower1+flower2)%2


def minesweaper():
    # create field
    r, c, n = (int(i) for i in input().split())  # r - rows, c - columns, n - mines
    field = [[0 for i in range(c)] for j in range(r)]
    # print(field)
    for i in range(n):
        rm, cm = (int(i) - 1 for i in input().split())
        field[rm][cm] = -1
    # print(field)
    for i in range(r):
        for j in range(c):
            if field[i][j] == 0:
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        field_i = i + di
                        field_j = j + dj
                        if 0 <= field_i < r and 0 <= field_j < c and field[field_i][field_j] == -1:
                            field[i][j] += 1
    for i in range(r):
        for j in range(c):
            if field[i][j] == -1:
                print("*", end="")
            elif field[i][j] == 0:
                print(".", end="")
            else:
                print(field[i][j], end="")
        print()


def cancelThan0():
    n = int(input())
    sum = n
    q = n ** 2
    while sum:
        n = int(input())
        q += n ** 2
        sum += n
    print(q)


def seq():
    n = int(input())
    m = []
    for i in range(n):
        c = 0
        while c < i + 1:
            m.append(i + 1)
            c += 1
            if n == len(m):
                print(*m)
                break


def posFinder():
    lst = [int(i) for i in input().split()]
    x = int(input())
    j = 0
    c = 0
    for i in lst:
        if x == i:
            c += 1
            print(j, end=' ')
        j += 1
    if c == 0:
        print("Отсутствует")


import copy


def matrix():
    a = [[int(i) for i in input().split()]]
    b = input()
    while b != 'end':
        a.append([int(i) for i in b.split()])
        b = input()
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i - 1][j] + a[i - len(a) + 1][j] + a[i][j - 1] + a[i][j - len(a[i]) + 1], end=" ")
        print()
        # a[i][j] = a[i - 1][j] + a[i + 1][j] + a[i][j - 1] + a[i][j + 1]


def spiral():
    n = int(input())
    if n > 1:
        count = 1
        shift = 0
        matrix = [[0 for i in range(n)] for j in range(n)]
        edge = count
        while count <= n ** 2:
            for i in range(shift, n - shift - 1):
                matrix[shift][i] = count
                edge = count + n - 2 * shift - 1
                matrix[i][n - 1 - shift] = edge
                count += 1
            count = edge + 1
            for i in range(n - shift - 1, shift, -1):
                matrix[n - shift - 1][i] = count
                edge = count + n - 2 * shift - 1
                matrix[i][shift] = edge
                count += 1
            count = edge + 1
            shift += 1
            if count == n ** 2:
                matrix[int(((n - 1) / 2))][int(((n - 1) / 2))] = count
                break
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                print(matrix[i][j], end="\t")
            print()
    else:
        print(n)


def spinShort():
    n = int(input())
    t = [[0] * n for i in range(n)]
    i, j = 0, 0
    for k in range(1, n * n + 1):
        t[i][j] = k
        if k == n * n:
            break
        if i <= j + 1 and i + j < n - 1:
            j += 1
        elif i < j and i + j >= n - 1:
            i += 1
        elif i >= j and i + j > n - 1:
            j -= 1
        elif i > j + 1 and i + j <= n - 1:
            i -= 1
    for i in range(n):
        print(*t[i])


def middle():
        s = 'A3333'
        # if len(s)%2:
        #     print(s[int(len(s) / 2)])
        # else:
        #     print(s[int(len(s)/2 - 1)] + s[int(len(s) / 2)])
        print((s[int(len(s) / 2)]) if len(s)%2 else s[int(len(s)/2 - 1)] + s[int(len(s) / 2)])


def pellNumbers(n):
    if n < 3:
        return n
    else:
        return 2 * pellNumbers(n - 1) + pellNumbers(n - 2)

def flip(d,a):
    print(sorted(a) if d == 'R' else sorted(a, reverse=True))
    # print(a)

def make_readable():
    seconds = 86399
    hh = seconds//3600
    mm = (seconds - 3600*hh)//60
    ss = seconds - 3600*hh - 60*mm
    print("{:02}:{:02}:{:02}".format(hh, mm, ss))


def phoneNubmer():
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    c = 0
    s = '('
    while c < 3:
        s += str(n[c])
        c += 1
    s += ') '
    for i in range(3, len(n)):
        s += str(n[i])
        if i == 5:
            s += '-'
    print(s)
    # return "({}{}{}) {}{}{}-{}{}{}{}".format(*n) # one-line solution


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # whileCycle()
    # whileCycle2()
    # sumOnInterval(a = int(input('Input a: ')), b = int(input('Input b: ')))
    # sumTillZero()
    # sumTillZero2()
    # slicePie()
    # breakContinue()
    # breakContinue2()
    # breakContinue3()
    # forRange()
    # printStars()
    # multiplyTable()
    # multiplyTable2()
    # sumOfOddBetween()
    # avg3()
    # avg3_2()
    # stringMethods()
    # slicing()
    # polindrom()
    # shortGenom()
    # sumOfSplitList()
    # sumOfNeighbours()
    # showRepited()
    # listKata()
    # listFiltering()
    # lovefunc()
    # minesweaper()
    # cancelThan0()
    # seq()
    # posFinder()
    # matrix()
    # spiral()
    # spinShort()
    # middle()
    # print(pellNumbers(5))
    # flip('R', [3, 2, 1, 2])
    # make_readable()
    phoneNubmer()