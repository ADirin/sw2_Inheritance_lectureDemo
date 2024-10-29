# Define the Person class
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return f"I am {self.name}, {self.age} years old, {self.gender}."


# Define the Member class, inheriting from Person
class Member(Person):
    def __init__(self, name, age, gender, membership_id):
        super().__init__(name, age, gender)
        self.membership_id = membership_id

    def introduce(self):
        return f"{super().introduce()} My membership ID is: {self.membership_id}."


# Define the Author class, inheriting from Person
class Author(Person):
    def __init__(self, name, age, gender, books_written):
        super().__init__(name, age, gender)
        self.books_written = books_written

    def list_books(self):
        return f"Books written: {', '.join(self.books_written)}"


# Define the AuthorMember class, inheriting from both Member and Author
class AuthorMember(Member, Author):
    def __init__(self, name, age, gender, membership_id, books_written):
        Member.__init__(self, name, age, gender, membership_id)
        Author.__init__(self, name, age, gender, books_written)

    def introduce(self):
        return f"{super().introduce()} {self.list_books()}"


# Create some AuthorMember instances
library_members = [
    AuthorMember("Alice", 30, "Female", "M001", ["The Hidden Forest", "Midnight Sun"]),
    AuthorMember("Bob", 45, "Male", "M002", ["Journey to Mars", "Galactic Encounters"]),
    AuthorMember("Carol", 28, "Female", "M003", ["Cooking with Spices", "The Art of Baking"]),
]

# Print introductions for each AuthorMember
for member in library_members:
    print(member.introduce())
