import random


def rand_nums():
    while True:
        number = random.randint(-9999, 9999)
        yield number


print('Длина списка:')
n = int(input())
cnt_odd = 0
cnt_even = 0
rnit = rand_nums()
for i in range(n):
    a = next(rnit)
    print(a, end=' ')
    if abs(a) % 2 == 0:
        cnt_even += 1
    else:
        cnt_odd += 1
print('\n', 'Четных:', cnt_even, '\n', 'Нечетных:', cnt_odd)
