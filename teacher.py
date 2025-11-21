
from person import Person
from address import Address


class Teacher(Person):

    date: str

    def __init__(self, firstName: str, lastName: str, age: int, date: str, address: Address):
        """
         Initialize a Teacher object.
        """
        super().__init__(firstName, lastName, age)
        self.date = date
        self.address = address


    def set_address(self, road: str, city: str, zipCode: int):
        """
         Set the address of the teacher.
        """
        self.address = Address(road, city, zipCode)


    def get_date(self):
        """
         Get the hire date of the teacher.
        """
        return self.date
    

    def __str__(self):
        """
         Return a string representation of the teacher.
        """
        return (f"Teacher{{"
            f"name : {self.getFullName()}', "
            f"age : {self.getAge()}, "
            f"hireDate : {self.date}, "
            f"road : {self.road}', "
            f"city : {self.city}', "
            f"zipCode : {self.zipCode}"
            f"}}")