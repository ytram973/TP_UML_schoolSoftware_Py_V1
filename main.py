from address import Address
from student import Student
from teacher import Teacher

jean = Teacher("jean", "dujardin", 34, "blabla", Address("bla", "bla", 12343))
alexandra = Student(1,"alexandra", "lamy", 32, Address("bla", "bla", 12343))

print(jean)
jean.set_address("tttt","rreerer",3232)
print(jean)
print(alexandra)