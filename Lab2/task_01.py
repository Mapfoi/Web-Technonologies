# 1. Чтение из командной строки произвольного набора
# параметров и определение для каждого параметра типа
# данных (дробное число, целое число, строка).

while True:
    inp = input("Enter something or 'exit': ")

    if inp.lower() == 'exit':
        break

    try:
        int_var = int(inp)
        print("input is int")
        continue
    except ValueError:
        pass

    try:
        float_var = float(inp)
        print("input is float")
        continue
    except ValueError:
        pass

    try:
        print("input is string")
    except ValueError:
        pass
