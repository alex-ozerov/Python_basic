indexes_tuple = (1, 2, 0, 2, 0, 1)
values_tuple = ('Пример-1', 'Пример-2', 'Пример-3')
result = tuple(values_tuple[idx] for idx in indexes_tuple)
print(result)