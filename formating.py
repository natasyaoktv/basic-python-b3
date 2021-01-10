# age = 20
# old = "tahun."
# txt = "Namaku Aca dan aku berumur {} {}".format(age, old)
# print(txt)

print("Menghitung luas persegi panjang")
#data type masih berupa string
# p = input("Masukkan Panjang: ")
# l = input("Masukkan Luas: ") 

#sudah berupa integer
p = int(input("Masukkan Panjang: ")) 
l = int(input("Masukkan Luas: ")) 

luas = int(p) * int(l) #kedua variable diubah menjadi integer

result = "Diketahui P = {} dan l = {}, maka luas persegi panjang adalah {}".format(p,l,luas)
print(result)