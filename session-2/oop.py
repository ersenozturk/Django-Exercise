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

""" class Person: 
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
person1.get_details() """

#! static method

""" class Person: 
    company = 'ersenDeveloperTeam'

    def set_details(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(self.name, self.age)

    @staticmethod
    def salute():
        print('hi there!!!')

person1 = Person()

print(person1.company)
person1.salute() """

#! special methods

""" class Person: 
    company = 'ersenDeveloperTeam'

    def __init__(self,name,age): # tanmlama yapar yapamz otomatik olarak çalışır
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'{self.name} {self.age}'

    def get_details(self):
        print(self.name, self.age)

person1 = Person('sahinder',29)
person1.get_details()

print(person1)  # __str__ dan sonra """

#---------------
#! encapsulation and abstraction (veriyi gizleme)

""" class Person: 
    company = 'ersenDeveloperTeam'

    def __init__(self,name,age): # tanmlama yapar yapamz otomatik olarak çalışır
        self.name = name
        self.age = age
        self._id = 5000   #gör ama değiştirme python için / private dir değişirse düzgün çalışamz
        self.__id2 = 5002   #erişilememe trick i
    
    def __str__(self):
        return f'{self.name} {self.age}'

    def get_details(self):
        print(self.name, self.age)

person1 = Person('mike', 33)
print(person1._id)
# print(person1.__id2)
print(person1._Person__id2)


#--
liste = [2,5,1,98,34,60,70]
print(liste.sort())
liste.sort()
print(liste)
#-- """

#! inheritance and polymorphism 

""" class Person: 
    company = 'ersenDeveloperTeam'

    def __init__(self,name,age): 
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'{self.name} {self.age}'

    def get_details(self):
        print(self.name, self.age)


class Employee(Person):

    def __init__(self,name,age,path): 
        # self.name = name
        # self.age = age
        super().__init__(name,age)
        self.path = path

    #?override
    def get_details(self):
        # print(self.name,self.age,self.path)
        super().get_details()
        print('look at 156 line-->', self.path)

emp1 = Employee('ersen',29, 'FS')
emp1.get_details() """

#! multiple inheritance

""" class Person: 
    company = 'ersenDeveloperTeam'

    def __init__(self,name,age): 
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'{self.name} {self.age}'

    def get_details(self):
        print(self.name, self.age)

class Lang:
    def __init__(self, langs):
        self.langs = langs

    def display_langs(self):
        print(self.langs)

class Employee(Person, Lang):
    def __init__(self,name,age,path, langs): 
        # self.name = name
        # self.age = age
        super().__init__(name,age)
        self.path = path
        # self.langs = langs
        Lang.__init__(self, langs)

    #?override
    def get_details(self):
        # print(self.name,self.age,self.path)
        super().get_details()
        print('look at 156 line-->', self.path)

emp1 = Employee('ersen',29, 'FS', ['python', 'js'])
emp1.get_details()
emp1.display_langs() 

print(Employee.mro())
"""
#--------

