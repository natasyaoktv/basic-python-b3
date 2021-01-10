angka = "ini adalah angka 10"
angka_list = ["ini", "adalah", "angka", "10"]


print(angka)
print(len(angka))
print(len(angka_list))

#append = menambahkan suatu data tanpa menghapus data yg ada di dalam list

print("data sebelumnya: ")
print(angka_list)

print("data setelah ditambahkan: ")
angka_list.append("loh iki")
print(angka_list)

angka_list[3] = 100 #mengganti index ke 3
print(angka_list)
