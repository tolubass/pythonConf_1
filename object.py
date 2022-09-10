class Students:
    def __init__(self,name, test1, test2, examscore):
        self.studentname = name
        self.test1 = test1
        self.test2 = test2
        self.examscore = examscore
    def totalTest(self):
        total = self.test1 + self.test2
        return total
    def genTotal(self):
        gen = self.examscore + self.totalTest()
        return gen
    def grade(self):
        grad = "F"
        y = self.genTotal()
        if y >= 70 and y <= 100:
            grad = "A"
        elif y >= 60 and y <= 70:
            grad = "B"
        elif y >= 50 and y < 60:
            grad = "c"
        elif y >= 45 and y < 50:
            grad = "D"
        elif y >= 40 and y < 44:
            grad = "E"
        elif y > 0 and y < 39:
            grad = "F"
        else:
            grad = "F"
        return grad

class Results(Students):
    def __init__(self,name, test1, test2, examscore):
        super(Results, self).__init__(name, test1, test2, examscore)
    def display(self):
        r = self.studentname + "----" + str(self.test1) + "----" + str(self.test2) + "----" + str(self.totalTest()) + "----" + str(self.examscore) + "----" + str(self.genTotal())+ "----" + str(self.grade())
        return r
