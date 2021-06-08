import json

goods = ["морковь", "картофель", "лук"]

json_goods = 'additional_task.json'


with open(json_goods, 'w') as file:
    json.dump(goods, file)

with open(json_goods, 'r') as file:
    read_data = json.load(file)
print(read_data)
