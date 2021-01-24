class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sapa(self):
        print("Halo namaku " + self.name)
        print("Umur {}".format(self.age))

class Employee(Person):
    def __init__(self, name, age, dob, golodar):
        self.dob = dob
        self.golodar = golodar

        Person.__init__(self,name,age)
    def printing(self):
        print("Nama: " + self.name)
        print("Umur: {}".format(self.age))
        print("Date of Birth: " + self.dob)
        print("Golongan darah: " + self.golodar)

a = Employee("Aca", 20, "1 0kt 2000", "A")
a.sapa()
a.printing()
