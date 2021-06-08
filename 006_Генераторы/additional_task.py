def my_gen():
    for i in range(n):
        k = 0
        for j in range(1, i):
            if i % j == 0:
                k = k + 1
        if k == 1:
            yield i


n = int(input("Введите n:"))


a = my_gen()
while True:
    try:
        print(next(a))
    except StopIteration:
        break
