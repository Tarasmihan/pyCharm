# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import math

def whileCycle():
    i = 0
    print("whileCycle_result: ", end = ' ')
    while i <= 10:
        print(i, end = ' ')
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


def sumTillZero2(): # pretty solution
    print('***sumTillZero2***')
    s = 0                            
    i = 1                            
    while i:                         
        i = int(input())             
        s += i                       
    print("sumTillZero2_result: ", s)


def slicePie(): # divide prize belong 2 teams
    print("***slicePie***")
    a = int(input("a: "))
    b = int(input("b: "))
    d = a
    while d%a or d%b:
        d += a
    print("slicePie_result: ", d)


def breakContinue():
    i = 0
    while i < 5:
        a, b = input().split()
        a = int(a)
        b = int(b)
        if (a==0) and (b==0):
            break
        if (a==0) or (b==0):
            continue
        print(a*b)
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
        print(n*'*')

def multiplyTable():
     a = int(input())
     b = int(input())
     c = int(input())
     d = int(input())
     print ('\t', end = '')
     for m in range(c, d+1):
         print(m, end = '\t')
     for i in range(a, b+1):
        print('\n')
        print(i, end ='\t')
        for j in range(c, d+1):
            print(i*j, end = '\t')

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
    for i in range (a, b+1, 2):
        s += i
    print(s)



def avg3():
    a = int(input())
    b = int(input())
    s = 0
    k = 0
    for i in range(a, b+1):
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
    for i in range (a, b+1, 3):
        s += i
    print(s)
    

def stringMethods():
    s = input().lower()
    t = s.count('c') + s.count('g')
    print(t/len(s) * 100)


def slicing():
    s = 'qwerty'
    s[1]     #w
    s[1:4]   #wer
    s[:4]    #qwer
    s[4:]    #ty
    s[-4:]   #erty
    s[1:-1]  #wert
    s[1:-1:2]#wr от первого до предпоследнего с шагом 2
    s[::-1]  #ytrewq
    k = 'abcdefghijk'
    print(k[3:6], end = ' ')
    print(k[:6], end = ' ')
    print(k[3:], end = ' ')
    print(k[::-1], end = ' ')
    print(k[-3:], end = ' ')
    print(k[:-6], end = ' ')
    print(k[-1:-10:-2]) 

def polindrom():
    polindrom_string = input('Первая строка: \t')
    x = polindrom_string[:math.ceil((len(polindrom_string)-1)/2)]
    y = polindrom_string[:math.ceil(len(polindrom_string)/2)-1:-1]
    print(x, y)
    print("y" if x == y else "n" )

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # whileCycle()
    # whileCycle2()
    # sumOnIntterval(a = int(input('Input a: ')), b = int(input('Input b: ')))
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
    shortGenom()
