from mashumaro import DataClassDictMixin
from dataclasses import dataclass

@dataclass
class Person(DataClassDictMixin):
    name: str
    age: int

person = Person(name="Alice", age=30)
person_dict = person.to_dict()
print(person_dict)  # {'name': 'Alice', 'age': 30}

