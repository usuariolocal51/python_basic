class Student:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


s1 = Student("Pepe", "Lucho")
s2 = Student("Pepa", "Pig")

studentList = []
studentList.append(s1)
studentList.append(s2)

print(studentList)

for std in studentList:
    print(std.name)

