def fib(n):
    if n < 2:
        if n == 0:
            return 0
        else:
            return 1
    else:
        res0 = fib(n - 1) + fib(n - 2)
        return res0


num = int(input())
res = fib(num - 1)
print('n-ое число фббфбфб:', res)