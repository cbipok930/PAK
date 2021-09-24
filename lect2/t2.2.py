str_in = input()
str = str_in
dct = {}
idx = str.find(' ')
max = 0
while idx != -1:
    word = list(str)[:idx]
    str = ''.join(list(str)[(idx + 1):len(str)])
    if len(word) > 0:
        new_pair = {len(word) : ''.join(word)}
        dct.update(new_pair)
        if len(word) > max:
            max = len(word)
    idx = str.find(' ')
longest = dct.get(max)
print('\"', longest, '\" - самое длинное слово в строке \"', str_in, '\"')
