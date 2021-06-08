class Rectangle():
    def input_rectangle(self):
        for i in range(10):
            print("." * 10)

class Mouse():
    def click_mouse(self):
        print("Нажатие кнопки")

class Button(Rectangle, Mouse):
    pass

click_button = Button()
click_button.input_rectangle()
click_button.click_mouse()

