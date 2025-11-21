from person import Person

class Student(Person):

    number: int

    def __init__(self, number: int, firstName: str, lastName: str, age: int, road: str, city: str, zipCode: int):
        super().__init__(firstName, lastName, age)
        self.number = number
        self.set_address(road, city, zipCode)
        self.lessons = []

    def set_address(self, road: str, city: str, zipCode: int):
        self.road = road
        self.city = city
        self.zipCode = zipCode

    def get_number(self):
        return self.number
    
    def set_number(self, number: int):
        self.number = number

    def add_lesson(self, lesson: str):
        if lesson is None:
            raise ValueError("Lesson cannot be None")
        
        if lesson not in self.lessons:
            self.lessons.append(lesson)
        
    def get_lessons(self):
        return self.lessons

    def __str__(self):
        return (f"Student{{"
            f"number : {self.number}, "
            f"name : {self.getFullName()}', "
            f"age : {self.getAge()}, "
            f"road : {self.road}', "
            f"city : {self.city}', "
            f"zipCode : {self.zipCode}"
            f"}}")
    
    