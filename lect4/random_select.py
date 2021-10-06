import os
import argparse
import numpy as np


def read(path):
    with open(path) as f:
        line = f.readline()
        lst = []
        flag = 1
        while len(line) != 0:
            if line[0] == '-':
                line = ''.join(list(map(lambda x: '' if x == '-' else x, line)))
                flag = -1
            lst = lst + (line.split())
            if lst[len(lst) - 1] == '\n':
                lst.pop(len(lst) - 1)
            line = ""
        lst = list(map(lambda x: int(x) * flag, lst))
    return lst


def foo1(a):
    if np.random.rand() > P:
        return a[0]
    else:
        return a[1]


def foo2(it):
    a = list(map(lambda x: real[int(x)] if (np.random.rand() > P) else im[int(x)], it))
    return np.array(a)


def m1(rr, ii):
    res = np.vstack((rr, ii))
    res = np.apply_along_axis(foo1, axis=0, arr=res)
    # print(res)
    return res


def m2(arr_size):
    res = np.fromfunction(foo2, (arr_size,))
    # print(res)
    return res


parser = argparse.ArgumentParser()
parser.add_argument("r_path", type=str, help='Путь к файлу с реальными данными')
parser.add_argument("i_path", type=str, help='Путь к файлу с синтетическими данными')
parser.add_argument("prb", type=float, help='Вероятность содержания синтетических данных')
parser.add_argument("way", nargs='?', const=1, type=int, help="Способ выполнения скрипта")
args = parser.parse_args()
P = args.prb
way = args.way
if way is None:
    way = 1
real_p = os.path.abspath(args.r_path)
im_p = os.path.abspath(args.i_path)
real = np.array(read(real_p))
im = np.array(read(im_p))
size = real.size
if size != im.size:
    print('Массивы разных размеров')
    exit()
n = 999999
p_test = 0
for i in range(n):
    if way == 1:
        arr = m1(real, im)
    else:
        arr = m2(size)
    arr = arr.tolist()
    s = 0
    for x in arr:
        if x < 0:
            s += 1
    p_test += s/size
    if i % 5000 == 0:
        print(i, '\\', n)
p_test/=n
print (p_test)