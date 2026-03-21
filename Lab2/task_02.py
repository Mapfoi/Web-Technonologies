# 2.	Генерацию HTML-таблицы с указанным количеством строк
# (передаётся как параметр командной строки); в каждой
# строке таблицы должен быть указан её номер.

MyPass = False
rows = None

while not MyPass:
    try:
        rows = int(input())
        MyPass = True
    except ValueError:
        print("Please enter a positive integer")
        continue

html = '<table border="1">\n'
# Header of the table made in first row
html += '  <tr><th>№</th><th>Содержимое</th></tr>\n'

for i in range(1, rows + 1):
    # <td> - table data
    html += f'  <tr><td>{i}</td><td></td></tr>\n'

html += '</table>'

print(html)
