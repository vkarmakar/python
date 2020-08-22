
class person:
  def __init__(self, name, age, location):
    self.name = name
    self.age = age
    self.location = location
  def detail(self):
    print(self.name, " is ", self.age, " years old and lives in ", self.location)

person('Vivek', 44, 'Kolkata').detail()
