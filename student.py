from person import Person
from address import Address

class Student(Person):

    number: int

    def __init__(self, number: int, firstName: str, lastName: str, age: int, address: Address):
        """
         Initialize a Student object.
        """
        super().__init__(firstName, lastName, age)
        self.number = number
        self.address = address
        self.lessons = []


    def set_address(self, road: str, city: str, zipCode: int):
        """
        Set the address of the student.
        """
        self.address = Address(road, city, zipCode)


    def get_number(self):
        """
         Get the student number.
         """
        return self.number
    

    def set_number(self, number: int):
        """
         Set the student number.
        """
        self.number = number


    def add_lesson(self, lesson: str):
        """
         Add a lesson to the student's list of lessons.
         """
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
            f"name : {self.getFullName()}', "
            f"age : {self.getAge()}, "
            f"road : {self.road}', "
            f"city : {self.city}', "
            f"zipCode : {self.zipCode}"
            f"}}")
    
    