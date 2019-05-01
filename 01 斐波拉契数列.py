lst = []
def fib(num):
    if num == 1:
        lst.append(1)
    elif num == 2:
        lst.append(1)
    else:
        lst.append(lst[num - 1] + lst[num - 2])
    return lst[len(lst)-1]


num = fib(100)
print(num)
