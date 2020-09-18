"""
CP1404 Practical 06
Gauvan Santiago

"""


class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        """initialise programming language, name, typing, reflection and year"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """returns data as a string"""
        return "{}, {} typing , reflection ={}, First appeared in {} ".format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        """ checks if programming language is dynamic"""
        return self.typing == "Dynamic"


