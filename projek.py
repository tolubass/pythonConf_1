class Students:
    def __init__(self, name, level, matric, hostel):
        self.name = name
        self.level = level
        self.matric = matric
        self.hostel = hostel
        print(f"My name is {self.name}")
        print(f"i am in part  {self.level}")
        print(f"from department of microbiology matric number of {self.matric}")
        print(f"i stay in {self.hostel}")
student_jk = Students("Olowolaju Tolulope", 3, "Mcb/2016/426", "Awolowo hall.")

a = input("Enter a valid integer:")
b = input("Enter another valid integer:")
c = int(a)/int(b)
print(f"The result of a/b is :{c}")
print("The program completes successfully.")

