import codecs

import numpy as np
import pandas as pd


def parse_row(rowp):
    # замена "Не указано" на '-' 2/8
    if ''.join(rowp[1]).find('"') != -1:
        new_el = '-'
        rowp = rowp[:1] + (rowp[3:])
        rowp.insert(1, new_el)
    # где не указан ряд, вставляем NaN 3/8
    if ''.join(rowp[2]).find('.') == -1:
        rowp.insert(2, 'NaN')
    # выравниваем значения в кавычках
    if ''.join(rowp[5]).find('"') != -1 and ''.join(rowp[6]).find('"') != -1:
        new_el = ' '.join(f'{w}' for w in [rowp[5], rowp[6]])
        rowp = rowp[:5] + (rowp[7:])
        rowp.insert(5, new_el)
    return rowp


with codecs.open("titanic_with_labels.csv", encoding='utf-8') as f:
    idxes = f.readline().split()
    df = pd.DataFrame([], columns=idxes)
    row = f.readline().split()
    while len(row) != 0:
        if row[0] == '144':
            a = 1
            a+=1
        row = parse_row(row)
        if int(row[0]) % 1500 == 0:
            print('Doing DataFrame...')
        row = pd.DataFrame(np.array([row[1:]]), columns=idxes, index=[row[0]])
        df = df.append(row)
        row = f.readline().split()
print(df.head(15))
df.to_csv('titanic.csv', index=False)
