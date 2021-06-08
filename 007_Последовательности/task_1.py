def arifm(*args):
    result = sum(args) / len(args)
    return result


list_ = [i for i in range(5)]

print(arifm(2, 4))
print(arifm(*list_))

