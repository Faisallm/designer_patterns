# factory is an object specialized in creating other objects.

class Dog:
    """A simple dog class"""
    
    def __init__(self, name):
        self._name = name
        
    def speak(self):
        return "Woof!"
    
      
class Cat:
    """A simple cat class"""
    
    def __init__(self, name):
        self._name = name
        
    def speak(self):
        return "Meow!"
    
def get_pet(pet="dog"):
    """The Factory Method"""
        
    pets = dict(dog=Dog("Hope"), cat=Cat("Mischief"))
    return pets[pet]

# we are using a function to easily create out object.
# without worrying about the various implementation classes of the object.

d = get_pet("dog");
print(d.speak())
print(d._name)

e = get_pet("dog");
print(e.speak())
print(e._name)

c = get_pet("cat")
print(c.speak())
print(c._name)