from address import Address
from person import Person
from address import Address


class Teacher(Person):
    date: str

    def __init__(self, firstname: str, lastname: str, age: int, date: str, address: Address):
        super().__init__(firstname, lastname, age, address)
        self.date = date

    def get_date(self) -> str:
        return self.date

    def __str__(self):
        """
         Return a string representation of the teacher.
        """
        return (f"Teacher{{"
                f"name : {self.get_fullname()}', "
                f"age : {self.get_age()}, "
                f"hireDate : {self.date}, "
                f"road : {self.address.road}, "
                f"city : {self.address.city}, "
                f"zipCode : {self.address.zip_code}"
                f"}}")
