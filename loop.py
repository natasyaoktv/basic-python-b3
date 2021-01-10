angka_list = ["ini", "adalah", "angka", "10"]

print("Example 1")
for x in angka_list:
    print(x)

print("Example 2")
hasil = ""
for x in range(0, len(angka_list)):
    hasil = hasil + angka_list[x]
    print(hasil)

print("Example 3")
for i in range(0,5): #harus menentukan range dari looping
    print("i ke: {}".format(i))

print("Example 4")
hasil = " "
for x in range(0, len(angka_list)): #rangenya adalah 0 sampai (banyaknya data dalam angka_list)
    hasil = hasil + " " + angka_list[x]
print(hasil)

print("Example 5")
for x in range(0,len(angka_list)): #x disini akan print index dari list_angka
    print(x)

print("Example 6")
for x in angka_list: #x disini akan print isi dari index dalam list_angka
    print(x)

print("Example 7")
number = 0
for x in range(0,len(angka_list)): #rangenya adalah 0 sampai (banyaknya data dalam angka_list)
    number = number + 1
    print(number)