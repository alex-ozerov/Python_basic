class Editor():
    def view_document(self):
        print("Документ доступен только для чтения!")

    def edit_document(self):
        print("Редактирование документов недоступно для бесплатной версии!")


class ProEditor(Editor):
    def edit_document(self):
        print("Доступ разрешен")



key = int(input("введите ключ"))
if key == 904:
    user1 = ProEditor()
    user1.edit_document()
else:
    user1 = Editor()
    user1.view_document()
    user1.edit_document()
