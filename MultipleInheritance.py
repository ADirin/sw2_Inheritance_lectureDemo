class Person:
    count = 0
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Person.count += 1

    def introduce(self):

        return f"Hello iam  + {self.name}, and my age is {self.age}, {self.gender} "

class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id

    def introduce(self):
        return f"{super().introduce()}, my student_id is {self.student_id}"


class Athlete:
    def __init__(self, sport, achievements):
        self.sport = sport
        self.achievements = achievements

    def athlete_info(self):
            return f"I play {self.sport}, and have acheived:  {', '.join(self.achievements)}"


class StudentAthlete(Student, Athlete):
    def __init__(self, name, age, gender, student_id, sport, achievements):
        Student.__init__(self, name, age, gender, student_id)
        Athlete.__init__(self, sport, achievements)
    def introduce(self):
        return f"{super().introduce()} and I am also an athlete: {self.athlete_info()}"

students =[]
student1 = StudentAthlete("John", "25", "Male", student_id="std01", sport="Basketball", achievements=["MVP", "All-Star"])
student2 = StudentAthlete("Matti", "25", "Female", student_id="std02", sport="Tennis", achievements=["Champion", "Semi-finalist"])
student3 = StudentAthlete("Kelly", "25", "Male", student_id="std03", sport="Swimming", achievements=["Gold Medal", "Record Holder"])

students.append(student1)
students.append(student2)
students.append(student3)
for student in students:
    print(student.introduce())





