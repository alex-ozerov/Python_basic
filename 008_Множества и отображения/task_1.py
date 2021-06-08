list1 = 'Я строка, и я  неизменяемая'
list2 = 'Я кортеж и я тоже неизменяемая'
result = set(list1).intersection(list2)
print(result)