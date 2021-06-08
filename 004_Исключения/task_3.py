class Employee():
    def __init__(self, name, surname, department, first_year):
        if not name:
            raise ValueError("Введенно не коректное значение!")
        if not surname:
            raise ValueError("Введенно не коректное значение!")
        if not department:
            raise ValueError("Введенно не коректное значение!")
        if not first_year:
            raise ValueError("Введенно не коректное значение!")
        self.name = name
        self.surname = surname
        self.department = department
        self.first_year = first_year

    def __repr__(self):
        return (f"name {self.name}, surname {self.surname}, department {self.department}, age {self.first_year}")


def filter_employee():
    list_employee_date = []
    for employee in  list_employee:
        if employee.first_year == "2020":
            list_employee_date.append(employee)
    print(list_employee_date)


list_employee = []


def main():
    global list_employee
    n = int(input("Введите количество сотрудников: "))
    for i in range(n):
        try:
            name = input("Введите имя сотрудника: ")
            surname = input("Введите фамилию сотрудника: ")
            department = input("Введите отдел сотрудника: ")
            first_year = input("Введите год поступления на работу сотрудника: ")
            employee = Employee(name, surname, department, first_year)
            list_employee.append(employee)
        except TypeError:
            print("Введенно не коректное значение!")
    print(list_employee)


if __name__ == "__main__":
    main()
    filter_employee()

