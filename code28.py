class Person:
    def __init__(people, name, age, sqesi):
        people.name = name
        people.age = age
        people.sqesi = sqesi
    def getinfo(people):
        print(people.name, people.age, people.sqesi)

dude = person ("dude", 10, "male")
dude2 = person ("dude2", 20, "female")
dude3 = person ("dude3", 30, "male")
dude4 = person ("dude4", 40, "female")
dude5 = person ("dude5", 50, "male")
dude6 = person ("dude6", 60, "female")
dude7 = person ("dude7", 70, "male")
dude8 = person ("dude8", 80, "female")

Persons =[dude, dude2, dude3, dude4, dude5, dude6, dude7, dude8]
for person in Persons:
    if person.age>60:
        person.getinfo()
