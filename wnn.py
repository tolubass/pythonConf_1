class Student:
    marks = []
    def getData(self, reg, name, m1, m2, m3):
        Student.reg = reg
        Student.name = name
        Student.marks.append(m1)
        Student.marks.append(m2)
        Student.marks.append(m3)
    def displayData(self):
        print ("reg number is:", Student.reg)
        print("name is:", Student.name)
        print ("Marks in test1: ", Student.marks[0])
        print("Marks are: ", Student.marks)

    def total(self):
        return(Student.marks[0] + Student.marks[1] +Student.marks[2])
