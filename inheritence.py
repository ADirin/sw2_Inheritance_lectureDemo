class person:
    count =0
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        person.count +=1


    def introduce(self):
        return f"I am {self.name}, and my age is: {self.age}, {self.gender}"

class student(person):

    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id

    def introduce(self):
        return f"{super().introduce()}, my student number is {self.student_id}"

students = []
student1=student("John", "25", "Male", student_id= "std01")
student2= student("Matti", "25", "Female", student_id= "std02")
student3= student("kelly", "25", "Male", student_id= "std03")
students.append(student1)
students.append(student2)
students.append(student3)

for student in students:
    print(student.introduce())
