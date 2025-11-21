from address import Address


class Person:

    def __init__(self, firstname: str, lastname: str, age: int, address: Address):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.address = address

    def set_address(self, road: str, city: str, zip_code: int) -> None:
        self.address.road = road
        self.address.city = city
        self.address.zipCode = zip_code

    def set_fullname(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

    def set_age(self, age: int) -> None:
        self.age = age

    def get_firstname(self) -> str:
        return self.firstname

    def get_lastname(self) -> str:
        return self.lastname

    def get_age(self) -> int:
        return self.age

    def get_fullname(self) -> str:
        return self.firstname + " " + self.lastname

    def get_road(self) -> str:
        return self.address.road

    def get_city(self) -> str:
        return self.address.city

    def get_zip_code(self) -> int:
        return self.address.zip_code
