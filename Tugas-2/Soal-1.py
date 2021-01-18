kontaknum = {
        "Nama: " : "Aca",
        "No Telepon: " : "081122288811"
}

def menu():
    print("--Menu--")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    print(" ")

def kontak():
    for x in kontaknum:
        print(x, kontaknum[x])

print("Selamat Datang!")
menu()
pilih = int(input("Pilih menu: "))
while pilih != 3:
    print(" ")
    if pilih == 1:
        print("Daftar Kontak")
        kontak()
        print("\n")
        menu()
    elif pilih == 2:
        print("Tambahkan Kontak")
        Nama = input("Masukkan nama: ")
        No = input("Masukkan nomor telepon: ")

        kontaknum["Nama :"] = Nama
        kontaknum["No Telepon :"] = No
        
        print("Kontak berhasil ditambahkan!")
        print("\n")
        menu()
    elif pilih > 3:
        print("Menu tidak tersedia!")
        print("\n")
        menu()
    pilih = int(input("Pilih menu: "))
print(" ")
print("Program selesai, sampai Jumpa!")

