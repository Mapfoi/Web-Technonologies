# 4. Подсчёт суммы цифр в числе, передаваемым как
# параметр командной строки (например, для числа
# 123 сумма цифр равна 6).

import sys


def sum_digits(number):
    res = 0
    while number > 10:
        res = res + number % 10
        number //= 10

    res += number
    return res


try:
    x = int(sys.argv[1])
    result = sum_digits(x)
    print(f"Sum of digits of number {x} = {result}")

except ValueError:
    print("Error: Please enter a valid integer")
    sys.exit(1)
