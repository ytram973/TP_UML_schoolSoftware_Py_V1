
from address import Address

class Person:

    def __init__(self, firstname: str, lastname: str, age: int, address: Address):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.address = address

        #Person.persons.append(self)

    def get_firstname(self) -> str:
        return self.firstname

    def get_lastname(self) -> str:
        return self.lastname

    def get_age(self) -> int:
        return self.age

    def get_fullname(self) -> str:
        return self.firstname + " " + self.lastname

    def get_road(self):
        return self.address.road

    def get_city(self):
        return self.address.city

    def get_zip_code(self):
        return self.address.zip_code

    def __repr__(self) -> str:
        return (f"{self.firstname}, "
                f"{self.lastname}, "
                f"{self.age}ans : "
                f"{self.address.road} "
                f"{self.address.zip_code} "
                f"{self.address.city}")

