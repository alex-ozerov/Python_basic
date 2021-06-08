keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = dict(zip(keys, values))

result_1 = {key: value for key in keys for value in values}

print(result, result_1)