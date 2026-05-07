def getinput(n1, n2):
    print('At function start id n1', id(n1))
    print('At function start id n2', id(n2))
    n1 = input('Enter a number')
    n2 = input('Enter a number')
    print('At function end id n1', id(n1))
    print('At function end id n2', id(n2))


def main():
    num1 = num2 = 0
    print('Before call function id n1', id(num1))
    print('Before call function id n2', id(num2))
    getinput(num1, num2)
    print('After call function id n1', id(num1))
    print('After call function id n2', id(num2))
    print(num1, num2)
    return num1, num2 


if __name__ == '__main__':
    main()
