str_in = input()
str = str_in.upper()
idx = str.rfind(' ')
while idx != -1:
    str_left = list(str)[:idx]
    str_right = list(str)[(idx + 1): len(str)]
    str_left.extend(str_right)
    str = ''.join(str_left)
    idx = str.rfind(' ')
str_cmp = ''.join(str_cmp)
if str_cmp == str:
    print("Строка \"", str_in, "\" является палиндромом")
else:
    print("Строка \"", str_in, "\" не является палиндромом")
