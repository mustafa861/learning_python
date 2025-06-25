from dataclasses import dataclass
from typing import ClassVar

@dataclass
class School:
    name: str
    age: int
    language : ClassVar[str] = "urdu"
    like_food : str
    national_food : ClassVar[str] = "Biryani"
    def student(self):
        return f"My name is {self.name} and my age is {self.age} and i speak in {School.language}"
    
    def eats(self):
        return f"my fav_food is {self.like_food}"
    
    @staticmethod
    def country():
        return f"the language is {School.language}"

    @staticmethod
    def eat(self):
        return f"The national food of pakistan is {School.national_food} "



print(School.country())
ali=School("mustafa" , 12)
print(ali)
print(ali.student())


