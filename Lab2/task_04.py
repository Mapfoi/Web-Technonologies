# 4. Подсчёт суммы цифр в числе, передаваемым как
# параметр командной строки (например, для числа
# 123 сумма цифр равна 6).

MyPass = False
x = None
while not MyPass:
    try:
        x = int(input())
        MyPass = True
    except ValueError:
        print("Please enter a positive integer")
        continue

res = 0
while x > 10:
    res = res + x % 10
    x //= 10

res += x
print(res)
