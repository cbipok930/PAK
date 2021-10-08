import os
import argparse
import numpy as np
import time


def read(path):
    with open(path) as f:
        line = f.readline()
        lst = []
        flag = 1
        while len(line) != 0:
            if line[0] == '-':
                line = ''.join(list(map(lambda z: '' if z == '-' else z, line)))
                flag = -1
            lst = lst + (line.split())
            if lst[len(lst) - 1] == '\n':
                lst.pop(len(lst) - 1)
            line = f.readline()
        lst = list(map(lambda x: int(x) * flag, lst))
    return lst


def foo1(a):
    if np.random.rand() > P:
        return a[0]
    else:
        return a[1]


# def foo2(it):
#     a = list(map(lambda z: real[int(z)] if (np.random.rand() > P) else im[int(z)], it))
#     return np.array(a)


def m1(just_useless_parameter):
    res = np.vstack((real, im))
    res = np.apply_along_axis(foo1, axis=0, arr=res)
    return res


def m2(arr_size):
    # res = np.fromfunction(foo2, (arr_size,))
    mask = np.random.rand(arr_size,)
    res = np.where(mask > P, real, im)
    return res


def m3(arr_size):
    mask = np.random.rand(arr_size, )
    mask = mask > P
    cond = [mask == True, mask == False]
    res = [real, im]
    res = np.select(cond, res)
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
ways = {1: m1,
        2: m2,
        3: m3}
real_p = os.path.abspath(args.r_path)
im_p = os.path.abspath(args.i_path)
real = np.array(read(real_p))
im = np.array(read(im_p))
size = real.size
if size != im.size:
    print('Массивы разных размеров')
    exit()
print(ways.get(way)(size))
print("Выполнить серию опытов? y/n")
ans = input()
if ans == 'y' or ans == 'Y':
    print(f'P = {P}\nКоличество опытов:')
    n = int(input())
    p_test = 0
    start = time.time()
    for i in range(n):
        arr = ways.get(way)(size)
        arr = arr.tolist()
        s = 0
        for x in arr:
            if x < 0:
                s += 1
        p_test += s / size
        if i % 5000 == 0:
            print(i, '\\', n)
    p_test /= n
    print(p_test, f"{ways.get(way)}\n отклонение: +-{abs(p_test - P)} при тестах = {n}\n время = {time.time() - start}")
