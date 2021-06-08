import os.path
values = [float(x) for x in open('task_1_1.txt').read().split()]
print(sum(float(i) for i in values))