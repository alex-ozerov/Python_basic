def my_gen(n):
    for i in range(n):
        k = 0
        for j in range(1, i):
            if i % j == 0:
                k = k + 1
        if k == 1:
            yield i

