

# WHILE CYCLE


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



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # WHILE CYCLE
    # whileCycle()
    # whileCycle2()
    # sumOnIntterval(a = int(input('Input a: ')), b = int(input('Input b: ')))
    # sumTillZero()
    # sumTillZero2()
    # slicePie()
    # BREAK CONTINUE

