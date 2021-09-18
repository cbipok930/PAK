import argparse


def func(number, a):
    b = number
    while True:
        b = b * a
        yield number


parser = argparse.ArgumentParser()
parser.add_argument("f_num", type=int, help='Первый член прогрессии')
parser.add_argument("q_arg", type=int, help='Знаменатель прогрессии')
parser.add_argument("nums", type=int, help='Количество эл прогрессии')
args = parser.parse_args()
first = args.f_num
q = args.q_arg
n = args.nums
func_gen = func(first, q)
for i in range(n):
    print((next(func_gen)), end=' ')
