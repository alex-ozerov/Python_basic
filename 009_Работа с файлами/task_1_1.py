import os.path
from random import randint

numbers = []
for i in range(10000):
    numbers.append(float(randint(1, 10000)) / 100)
str1 = " ".join(str(x) for x in numbers)


def input_numbers(task_1_1, str1):
    f = open(task_1_1, "w")
    f.write(str1)
    f.close()


if __name__ == '__main__':
    input_numbers(os.path.join('C:/Users/1/PycharmProjects/Python_basic/009_Работа с файлами', 'task_1_1.txt'), str1)

