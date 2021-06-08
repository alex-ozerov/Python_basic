import os.path

my_dict = {}
while True:
    start = str(input("Вы можете ввести ссылку и короткую ссылку к ней"
                      "(для этого нажмите кнопку input_link),\n"
                      "так же вы можете вывести сылку по её короткому названию(для этого нажмите кнопку short_link),\n"
                      "для того что бы заветшить программу введите exit:"))
    if start == "input_link":
        while True:
            short_link = input("Введите короткую ссылку:")
            link = input("Введите ссылку:")
            if not short_link:
                break
            my_dict[short_link] = link
        print(my_dict)
        f = open('task_2.txt', 'a')
        f.write(str(my_dict))
        f.close()
    elif start == "short_link":
        input_short_link = input("Введите короткую ссылку: ")
        print(my_dict.get(input_short_link))
    elif start == "exit":
        break
