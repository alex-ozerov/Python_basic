my_list = [1, 2, 35, 46, 5]

def my_gen():
    i = -1
    while i < len(my_list):
        i += 1
        yield my_list[::-1][i]


a = my_gen()

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
