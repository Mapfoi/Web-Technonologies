# 5. Чтение из командной строки произвольного количества
# слов (каждое слово – отдельный параметр командной строки)
# и определение самого длинного слова (или самых длинных слов,
# если таких окажется больше одного).

import sys

# Skipping first arg
all_args = sys.argv[1:]

maxlen = 0
answer = 0
for each_arg in all_args:
    if len(each_arg) > maxlen:
        maxlen = len(each_arg)
        answer = each_arg

if answer != 0:
    print(f"The longest word '{answer}' has {maxlen} characters")
