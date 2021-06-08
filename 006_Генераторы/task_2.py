my_list = [1, 2, 3, 4, 5]
list_ = [x ** 2 for x in my_list if x % 2 == 0]
print(list_)


list_ = []
for i in my_list:
    if i % 2 == 0:
        list_.append(i**2)
print(list_)
