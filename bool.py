#pertemuan 1
print(10<6)
print(10>6)
print(10==6)

#pertemuan 2
# a = 10
# b = 5

# < kurang dari
# > lebih dari
# == sama dengan
# >= lebih dari atau sama dengan 
# <= kurang dari atau sama dengan

# and -> kedua condition harus benar
# or -> salah satu condition benar
# != -> tidak sama dengan/bukan
# not -> bukan

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

if(a>b):
    print("a lebih besar dari b")
elif(a<b):
    print("a lebih kecil dari b")
else:
    print("a sama dengan b")

if(a%2==0):
    print("bilangan genap")
else:
    print("bilangan ganjil")

if(a%2==0 and b%2==0):
    print("Kedua angka adalah bilangan genap")
elif(a%2==0 or b%2==0):
    print("Salah satu angka adalah bilangan ganjil")
else:
    print("Kedua angka adalah bilangan ganjil")

c = int(input("Masukkan angka: "))

if(not(c%2==0)):
    print("Ganjil")
else:
    print("Genap")