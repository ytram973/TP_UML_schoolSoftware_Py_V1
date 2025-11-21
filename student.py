from address import Address
from person import Person
from address import Address


class Student(Person):
    number: int

    def __init__(self, number: int, firstname: str, lastname: str, age: int, address: Address):
        super().__init__(firstname, lastname, age, address)
        self.number = number
        self.lessons = []

    def get_number(self) -> int:
        return self.number

    def set_number(self, number: int) -> None:
        self.number = number

    def add_lesson(self, lesson: str) -> None:
        if lesson is None:
            raise ValueError("Lesson cannot be None")

        if lesson not in self.lessons:
            self.lessons.append(lesson)

    def get_lessons(self):
        """
        Get the list of lessons for the student.
        """
        return self.lessons


    def __str__(self):
        """
         Return a string representation of the student."""
        return (f"Student{{"
                f"number : {self.number}, "
                f"name : {self.get_fullname()}, "
                f"age : {self.get_age()}, "
                f"road : {self.address.road}, "
                f"city : {self.address.city}, "
                f"zipCode : {self.address.zip_code}"
                f"}}")
