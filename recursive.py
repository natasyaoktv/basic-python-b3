# def sapa():
#     print("Halo!!")
#     sapa()

# sapa()

def masukkan():
    inputan = input("Masukkan angka: ")
    if inputan == "Stop":
        print("Berhenti")
    else:
        masukkan()

masukkan()

def lanjut():
    inputan = input("Lanjut? \n")
    if inputan == "no":
        print("Berhenti")
    else:
        lanjut()

lanjut()