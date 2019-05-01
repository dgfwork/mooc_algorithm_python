
def fib(num):
    if num == 1 or num == 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


num = fib(10)
print(num)
