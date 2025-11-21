from datetime import date
from address import Address
from person import Person


class Teacher(Person):
    hire_date: date

    def __init__(self, firstname: str, lastname: str, age: int, hire_date: date, address: Address):
        super().__init__(firstname, lastname, age, address)
        self.hire_date = hire_date

    def get_date(self) -> date:
        return self.hire_date

    def __str__(self):
        """
         Return a string representation of the teacher.
        """
        return (f"Teacher{{"
                f"name : {self.get_fullname()}', "
                f"age : {self.get_age()}, "
                f"hireDate : {self.hire_date}, "
                f"road : {self.address.road}, "
                f"city : {self.address.city}, "
                f"zipCode : {self.address.zip_code}"
                f"}}")
    
    """Test push"""
