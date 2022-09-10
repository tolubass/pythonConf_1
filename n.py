class Student:
    marks = []
    def __init__(self,name, clas, test1, test2, examscore, total, grade):
        self.studentname = name
        self.myclass = clas
        self.test1 = test1
        self.test2 = test2
        self.examscore = examscore
        self.total = total
        self.grade = grade
    def displayData(self):
        print ("name is:", self.studentname)
        print("class is:", self.myclass)
        print ("Marks in test1: ", self.test1)
        print("Marks in test2: ", self.test2)
        print("Marks in examscore: ", self.examscore)
        print("total marks: ", self.total)
        print("grade: ", self.grade)

class Grades:
    def opera(z):
        grade = "F"
        y = z
        if y >= 70 and y <= 100:
            grade = "A"
        elif y >= 60 and y <= 70:
            grade = "B"
        elif y >= 50 and y < 60:
            grade = "c"
        elif y >= 45 and y < 50:
            grade = "D"
        elif y >= 40 and y < 44:
            grade = "E"
        elif y > 0 and y < 39:
            grade = "F"
        else:
            grade = "F"
        return grade

