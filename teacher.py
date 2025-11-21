
from person import Person


class Teacher(Person):

    date: str

    def __init__(self, firstName: str, lastName: str, age: int, date: str, road: str, city: str, zipCode: int):
        super().__init__(firstName, lastName, age)
        self.date = date
        self.set_address(road, city, zipCode)


    def set_address(self, road: str, city: str, zipCode: int):
        self.road = road
        self.city = city
        self.zipCode = zipCode

    def get_date(self):
        return self.date
    
    def __str__(self):
        return (f"Teacher{{"
            f"name : {self.getFullName()}', "
            f"age : {self.getAge()}, "
            f"hireDate : {self.date}, "
            f"road : {self.road}', "
            f"city : {self.city}', "
            f"zipCode : {self.zipCode}"
            f"}}")