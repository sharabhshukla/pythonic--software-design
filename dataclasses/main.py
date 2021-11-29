from dataclasses import dataclass


@dataclass(frozen=True)
class Person:
    name= 'Sharabh'
    age = 23
    sex = 'Male'







p1 = Person()
