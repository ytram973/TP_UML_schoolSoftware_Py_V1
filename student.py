from person import Person

class Student(Person):

    number = None

    

    def __init__(self, number, firstName, lastName, age, road, city, zipCode):
        super().__init__(firstName, lastName, age)
        self.number = number
        self.set_address(road, city, zipCode)
        self.lessons = []


    def set_address(self, road, city, zipCode):
        self.road = road
        self.city = city
        self.zipCode = zipCode

    def get_number(self):
        return self.number
    
    def set_number(self, number):
        self.number = number
    