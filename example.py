class Biodata:
    def __init__(self, name, age, bod, bloodtype):
        self.name = name
        self.age = age
        self.bod = bod
        self.bloodtype = bloodtype

    
    def bio(self):
        print("Halo namaku " + self.name)
        print("Umur " + self.age)
        print("Lahir pada " + self.bod)
        print("Golongan darah " + self.bloodtype)

name = input("Nama: ")
age = input("Umur: ")
bod = input("Tanggal lahir: ")
bloodtype = input("Golongan darah: ")

data = Biodata(name, age, bod, bloodtype)
data.bio()