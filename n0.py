class Student(object):
    def __init__(self, name, surname, age, grade, address):
        self.name=name
        self.surname=surname
        self.age=age
        self.grade=grade
        self.address=address

    name = input("Enter name")
    surname = input("Enter surname")
    age = input("Enter age")
    grade = input("Enter grade")
    address = input("Enter address")
        return Student(name, surname, age, grade, address)