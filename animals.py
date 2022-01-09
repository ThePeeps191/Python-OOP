class Animals:
  def __iniit__(self, name):
    self.name = name


class Dog(Animals):
  def bark(self):
    print("I barked!")

class Poodle(Dog):
  def hi(self):
    print("I am a poddle and I say hi!!!")

    
bob = Poddle("bob")
