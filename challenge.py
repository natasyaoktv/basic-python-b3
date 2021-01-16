number = int(input("How many? "))

name = []
age = []

for i in range(number):
    name.append(input("Masukkan nama: "))
    age.append(int(input("Masukkan umur: ")))

    print(" ")

for i in range(number):
    print("Data Pelanggan")
    print("Nama Pelanggan = {}".format(name[i]))
    print("Umur = {}".format(age[i]))

    print(" ")



   
