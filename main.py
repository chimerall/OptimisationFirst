import math

# Ввод номера функции
print('Функции: ')
print('1. (x-1)^2')
print('2. (4x^3) - 8x^2 - 11x + 5')
print('3. x + 3/x^2')
print('4. (x + 2,5) / (4 -x^2)')
print('5. -sin(x) - sin(3x)/3')
print('6. -2sin(x) - sin(2x) - 2sin(3x)/3')
numbFunc = int(input("Введите номер функции: "))

# Ввод номера метода
print('Методы: ')
print("1. Метод пассивного поиска")
print("2. Метод Фибоначчи")
numbMethod = int(input("Введите номер метода: "))

# Перечень функций
def func(x):
    if numbFunc == 1:
        return pow((x - 1), 2)
    elif numbFunc == 2:
        return 4 * pow(x, 3) - 8 * pow(x, 2) - 11 * x + 5
    elif numbFunc == 3:
        if x0 == 0:
            print('Пожалуйста, измените входное значение х0')
            exit()
        else:
            return x + (3 / (x ** 2))
    elif numbFunc == 4:
        if x0 == 2 or x0 == -2:
            print('Пожалуйста, измените входное значение х0')
            exit()
        else:
            return (x + 2.5) / (4 - pow(x, 2))
    elif numbFunc == 5:
        return -math.sin(x) - (math.sin(3 * x) / 3)
    elif numbFunc == 6:
        return -2 * math.sin(x) - math.sin(2 * x) - 2 * math.sin(3 * x) / 3

x0 = float(input("Введите X0: "))  # Начальная точка
h = float(input("Введите h: "))  # Шаг

# Метод Дэвиса-Свенна-Кэмпи
def dsk(x0, h, func):
    f0 = func(x0)   # Шаг 1
    a = 0   # Левая граница
    b = 0   # Правая граница
    k = 0   # Итерация
    if f0 > func(x0 + h):   # Шаг 2
        a = x0
        x0 += h
        k += 1
        f0 = func(x0)
    elif func(x0 - h) >= f0:    # Шаг 3
        a = x0 - h
        b = x0 + h
        return (a, b)   # Окончание поиска (шаг 6)
    else:
        b = x0
        h = -h
    # Шаг 4
    def xk(k: int):
        return x0 + (2 ** (k - 1)) * h

    def assign_if(is_a, value):
        nonlocal a, b
        if is_a:
            a = value
        else:
            b = value

    while True:
        xk0, xk1 = xk(k), xk(k - 1)
        # Шаг 5
        if func(xk0) >= func(xk1):
            assign_if(h < 0, xk0)
            break
        else:
            assign_if(h > 0, xk1)
        k += 1
    return (a, b)
res = dsk(x0, h, func)
print(res)

# Метод пассивного поиска
if numbMethod == 1:
    a = x = res[0]
    b = res[1]
    N = int(input('Введите количество отрезков: '))
    step = (b - a) / N  # Шаг 1
    def passive_search(a, b, N, func):
        min_f_x = func(x)
        min_x = a
        for i in range(N): # Шаг 2
            f_x = func(a+i*step)
            if f_x < min_f_x: # Шаг 3
                min_f_x = f_x
                min_x = a + i * step
        return (round(min_f_x * 1000) / 1000 , round(min_x * 1000) / 1000)

    result = passive_search(a,b,N,func)
    print('f(x*) = min f(x) = ', result[0])
    print('x* = ', result[1])

# Метод Фибоначчи
if numbMethod == 2:
    a = res[0]
    b = res[1]
    eps = float(input('Задайте параметр точности: '))
    sigma = eps / 10    # малая константа "различимости"
    #Шаг 1
    N = int((b - a) / (2 * eps))
    print('Количество вычислений функции как наименьшее целое', N)
    k = 0   # Итерация (шаг 2)
    class FibonacciImpl:    # Вычисление чисел Фибоначчи
        arr = [0, 1, 1]
        def calculate(self, num: int):
            if num < len(self.arr):
                return self.arr[num]
            else:
                for i in range(len(self.arr) - 1, num):
                    new_fib = self.arr[i - 1] + self.arr[i]
                    self.arr.append(new_fib)
                return self.arr[num]
    fib_impl = FibonacciImpl()
    def fib(num):
        global fib_impl
        return fib_impl.calculate(num)
    # Шаг 3
    x1 = a + fib(N - 2) / fib(N) * (b - a)
    x2 = a + fib(N - 1) / fib(N) * (b - a)
    for k in range(2, N - 2):   # Критерий останова k = N-3
        if func(x1) <= func(x2):    # Шаг 4,5
            b = x2
            x2 = x1
            x1 = a + fib(N - k - 3) / fib(N - k - 1) * (b - a)
        else:
            a = x1
            x1 = x2
            x2 = a + fib(N - k - 2) / fib(N - k - 1) * (b - a)
    # Шаг 6
    x2 = x1 + sigma
    if func(x1) <= func(x2):
        b = x2
    else:
        a = x1
    res1 = (a + b) / 2  # Шаг 7
    print(res1)