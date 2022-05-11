""" def print_type(data):
    for i in data:
        print(i,type(i))

test = [122, 'ersen', [1,2,3], (1,2,3), {1,2,3}, True]
print_type(test)

class Person: 
    name = 'ersen',
    age= 29

person1 = Person()
person2 = Person()

print(person1.name)
print(person2.name)

Person.job = 'developer'

print(person1.job) """

#! class attributes and instance attrbutes
""" 
class Person: 
    name = 'ersen',
    age= 29

person1 = Person()
person2 = Person()
person1.location = 'Turkey'
print(person1.location)  """

#! SELF keyword

class Person: 
    name = 'ersen'
    age= 29

    def test(self):
        print('testt')

    def set_details(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(self.name, self.age)


person1 = Person()

person1.get_details()
person1.set_details('gunes', 1)
person1.get_details()