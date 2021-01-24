def greeting(nama):
    print("Halo, " + nama)

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