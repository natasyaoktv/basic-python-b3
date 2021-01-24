#constructor penyebutan dirinya sendiri
class Person:
    def __init__(self, name, age, nama_lawan, age_lawan):
        self.name = name
        self.age = age
        self.nama_lawan = nama_lawan
        self.age_lawan = age_lawan

    def sapa(self):
        print("Halo namaku " + self.name)
        print("Umur {}".format(self.age))
        print("Namamu siapa?")
    
    def salamkenal(self):
        print("Salam kenal, saya " + self.nama_lawan)
        print("Umur {}".format(self.age_lawan))
        print("Senang berkenalan!")
import module

p1 = module.Person("Nafi", 22, "Dodit", 24)
p1.sapa()
p1.salamkenal()
# p1 = Person("Nafi", 22)
# p2 = Person("Dodit", 24)

# print(p1.name)
# print(p1.age)
# print(p2.name)
# print(p2.age)