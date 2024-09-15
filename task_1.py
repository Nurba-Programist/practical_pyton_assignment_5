def square_generator(N):
    for num in range(1, N + 1):
        yield num ** 2

# Ввод числа
N = int(input("Введите число: "))

# Использование генератора
for square in square_generator(N):
    print(square)

# Ввод числа
N = int(input("Введите число: "))

# Генераторное выражение
squares = (num ** 2 for num in range(1, N + 1))

# Использование генераторного выражения
for square in squares:
    print(square)