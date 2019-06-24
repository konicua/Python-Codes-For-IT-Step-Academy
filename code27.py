class Person:
  def init(self, name, age, sqesi):
    self.name = name
    self.age = age
    self.sqesi = sqesi
giorgi=Person("giorgi",27,"male")
giorgi1=Person("gogo",22,"female")
giorgi2=Person("nika",27,"male")

Persons =[giorgi,giorgi1,giorgi2]
for i in Persons:
        print(i.name,i.age,i.sqesi)