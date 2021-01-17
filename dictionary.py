# thisdic = {
#             "brand" : "Ford",
#             "model" : "Mustang",
#             "year" : 1964
#         }

# print(thisdic)

# bio = {
#         "Nama" : "Aca",
#         "Umur" : 20,
#         "Tinggi" : 168
#     }

# print(bio)
# print(bio["Nama"])

sekolah = {
            "Kelas7" : 30,
            "Kelas8" : 28,
            "Kelas9" : 40
}

# print("Jumlah anak kelas 7 adalah {}".format(sekolah["Kelas7"]))
# print("Jumlah anak kelas 8 adalah {}".format(sekolah["Kelas8"]))
# print("Jumlah anak kelas 9 adalah {}".format(sekolah["Kelas9"]))

# sekolah["Kelas8"] = 35
# print("Data baru jumlah anak sekolah kelas 8 adalah {}".format(sekolah["Kelas8"]))

for x in sekolah:
    print(x)

for x in sekolah:
    print(x)
    print(sekolah["{}".format(x)])

for x in sekolah:
    print("Jumlah anak {} adalah {}".format(x,sekolah[x]))
    
for x in sekolah:
    print(sekolah[x])