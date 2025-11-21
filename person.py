from typing import ClassVar


class Person:
    #persons = []

    def __init__(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        #Person.persons.append(self)

    def get_firstname(self) -> str:
        return self.firstname

    def get_lastname(self) -> str:
        return self.lastname

    def get_age(self) -> int:
        return self.age

    def get_fullname(self) -> str:
        return self.firstname + " " + self.lastname

    def __repr__(self) -> str:
        return f"{self.firstname}, {self.lastname}, {self.age}ans"

