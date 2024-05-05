def foo(a):
    return a ** 3

# print(foo(2))

lambda_f = lambda x: x ** 3
# print(lambda_f(2))

def foo2(number):
    if number % 2 == 1:
        return 'NO'
    else:
        return 'YES'

# print(foo2(4))

lambda_f2 = lambda number: 'no' if number % 2 == 1 else 'yes'
# print(lambda_f2(5))

list_a = [199, 2, 34, 909, -100, 18]
# print(list_a)
list_a.sort(key=lambda x: x % 10)
# print(list_a)

calc = {
    '+': lambda a, b: a+b,
    '-': lambda a, b: a-b,
    '*': lambda a, b: a*b,
    '/': lambda a, b: a/b,
}

print(calc.get('+')(2, 5))
