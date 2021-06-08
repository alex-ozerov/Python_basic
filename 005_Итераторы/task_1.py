iterable = [1, 2, 3, 4, 5]
iter_obj = iter(iterable)
while True:
    try:
        element = next(iter_obj)
        print(element)
    except StopIteration:
        break
