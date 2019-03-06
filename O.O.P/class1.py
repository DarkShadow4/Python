class Dog(object):
    """My fist class will be a dog."""
    def __init__(self, name, age):
        """Now i will initialize the atributes for name and age"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate that the dog is sitting"""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """Simulate that the dog rollsover"""
        print(self.name.title() + "rolled over!")

dog1 = Dog("Pipo", 999)
print "My dog's name is", dog1.name.title() + "."
print "My dog is",dog1.age, "years old."
