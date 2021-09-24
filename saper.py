import random
import argparse


def fill_cells_row(field, rownum, n, m):
    rowmode = 'edge_up' if (rownum == 0) else 'ein'
    rowmode = 'edge_dwn' if (rownum == n - 1) else rowmode
    maxx = 0
    if (field[rownum])[0] != '\u03A9':
        cnt = cnt_bombs(field, 0, rownum, rowmode, 'col_left')
        (field[rownum])[0] = cnt
        maxx = cnt if cnt > maxx else maxx
    for i in range(1, (m - 1)):
        if (field[rownum])[i] != '\u03A9':
            cnt = cnt_bombs(field, i, rownum, rowmode, 'cin')
            (field[rownum])[i] = cnt
            maxx = cnt if cnt > maxx else maxx
    if (field[rownum])[m - 1] != '\u03A9':
        cnt = cnt_bombs(field, m - 1, rownum, rowmode, 'col_right')
        (field[rownum])[m - 1] = cnt
        maxx = cnt if cnt > maxx else maxx
    return maxx


def cnt_bombs(field, x, y, rowmode, colmode):
    cnt = 0
    if rowmode == 'edge_up':
        if colmode == 'col_left':
            cnt = cnt_bombs_angles(field, x, y, 'plus', 'plus', cnt)
        elif colmode == 'col_right':
            cnt = cnt_bombs_angles(field, x, y, 'minus', 'plus', cnt)
        else:
            cnt = cnt_bombs_borders(field, x, y, 'none', 'plus', 'vertical', cnt)
    elif rowmode == 'edge_dwn':
        if colmode == 'col_left':
            cnt = cnt_bombs_angles(field, x, y, 'plus', 'minus', cnt)
        elif colmode == 'col_right':
            cnt = cnt_bombs_angles(field, x, y, 'minus', 'minus', cnt)
        else:
            cnt = cnt_bombs_borders(field, x, y, 'none', 'minus', 'vertical', cnt)
    elif colmode == 'col_left':
        cnt = cnt_bombs_borders(field, x, y, 'plus', 'none', 'horizontal', cnt)
    elif colmode == 'col_right':
        cnt = cnt_bombs_borders(field, x, y, 'minus', 'none', 'horizontal', cnt)
    else:
        cnt = (cnt + 1) if (field[y])[x + 1] == '\u03A9' else cnt
        cnt = (cnt + 1) if (field[y])[x - 1] == '\u03A9' else cnt
        cnt = (cnt + 1) if (field[y + 1])[x] == '\u03A9' else cnt
        cnt = (cnt + 1) if (field[y - 1])[x] == '\u03A9' else cnt
        cnt = (cnt + 1) if (field[y + 1])[x + 1] == '\u03A9' else cnt
        cnt = (cnt + 1) if (field[y + 1])[x - 1] == '\u03A9' else cnt
        cnt = (cnt + 1) if (field[y - 1])[x + 1] == '\u03A9' else cnt
        cnt = (cnt + 1) if (field[y - 1])[x - 1] == '\u03A9' else cnt
    return cnt


def cnt_bombs_angles(field, x, y, xm, ym, cnt):
    j = (x - 1) if (xm == 'minus') else (x + 1)
    i = (y - 1) if (ym == 'minus') else (y + 1)
    cnt = (cnt + 1) if (field[y])[j] == '\u03A9' else cnt
    cnt = (cnt + 1) if (field[i])[x] == '\u03A9' else cnt
    cnt = (cnt + 1) if (field[i])[j] == '\u03A9' else cnt
    return cnt


def cnt_bombs_borders(field, x, y, xm, ym, mode, cnt):
    j = (x - 1) if (xm == 'minus') else (x + 1)
    i = (y - 1) if (ym == 'minus') else (y + 1)
    if mode == 'horizontal':
        cnt = (cnt + 1) if (field[y])[j] == '\u03A9' else cnt
        cnt = (cnt + 1) if (field[y + 1])[x] == '\u03A9' else cnt
        cnt = (cnt + 1) if (field[y - 1])[x] == '\u03A9' else cnt
        cnt = (cnt + 1) if (field[y + 1])[j] == '\u03A9' else cnt
        cnt = (cnt + 1) if (field[y - 1])[j] == '\u03A9' else cnt
    else:
        cnt = (cnt + 1) if (field[y])[x + 1] == '\u03A9' else cnt
        cnt = (cnt + 1) if (field[y])[x - 1] == '\u03A9' else cnt
        cnt = (cnt + 1) if (field[i])[x] == '\u03A9' else cnt
        cnt = (cnt + 1) if (field[i])[x + 1] == '\u03A9' else cnt
        cnt = (cnt + 1) if (field[i])[x - 1] == '\u03A9' else cnt
    return cnt


def digits(a):
    if a == '\u03A9':
        return 1
    elif a == 0:
        return 1
    else:
        dcnt = 0
        while a > 0:
            dcnt+= 1
            a//= 10
    return dcnt


parser = argparse.ArgumentParser()
parser.add_argument("height", type=int, help='Высота поля')
parser.add_argument("width", type=int, help='Ширина поля')
parser.add_argument("bombs", type=int, help='Количество бомб')
args = parser.parse_args()
n = args.height
m = args.width
k = args.bombs
field = []
for i in range(0, n):
    lst = []
    for j in range(0, m):
        lst.append(int(0))
    field.append(lst)
if k <= n * m:
    while k > 0:
        x = random.randint(0, m - 1)
        y = random.randint(0, n - 1)
        if (field[y])[x] == 0:
            (field[y])[x] = '\u03A9'
            k -= 1
        else:
            continue
    max = 0
    for i in range(0, n):
        max1 = fill_cells_row(field, i, n, m)
        max = max1 if max1 > max else max
    cell = digits(max) + 1
    # вывод поля
    for i in range(0, n):
        print('[', end='')
        for j in range(0, m):
            if j < (n - 1):
                print((field[i])[j], ' ' *(cell - (digits((field[i])[j]))), end='|')
            else:
                print((field[i])[j], ' ' *(cell - (digits((field[i])[j]))), end='')
        print(']')
    u = '\u03A9'
    print(u)
else:
    print("Неверный формат: не хватает поля для бомб")