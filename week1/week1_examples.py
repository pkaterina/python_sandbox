def division(num1, num2):
    expr1 = str(num1) + ' // ' + str(num2)
    expr2 = str(num1) + ' % ' + str(num2)
    print(expr1, '=', eval(expr1), ' :: ', expr2, '=', eval(expr2))


def prepare_1():
    division(11, 5)
    division(11, -5)
    division(-11, 5)
    division(-11, -5)


def prepare_2():
    a = int(input())
    b = int(input())
    print(a + b)


def task_1():
    name = input()
    print('Hello, ', name, '!', sep='')


task_1()
