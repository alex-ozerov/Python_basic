list_of_strings = ["Список - изменяемый тип данных", "Строка - неизменяемый тип данных",
                   "Строковый метод работает быстрее, чем срез",
                   "Для обхода последовательности используйте совместный цикл"]
result = tuple(sequence for sequence in list_of_strings if 'тип данных' in sequence)
print(result)



list_of_strings = ["Список - изменяемый тип данных", "Строка - неизменяемый тип данных",
                   "Строковый метод работает быстрее, чем срез",
                   "Для обхода последовательности используйте совместный цикл"]
result = tuple(sequence for sequence in list_of_strings if not sequence.lower().startswith('с'))
print(result)


list_of_strings = ["Список - изменяемый тип данных", "Строка - неизменяемый тип данных",
                   "Строковый метод работает быстрее, чем срез",
                   "Для обхода последовательности используйте совместный цикл"]
result = tuple(word.lower() for sequence in list_of_strings for word in sequence.split(" ") if
               word.lower().startswith("с"))
print(result)