def hello():
    print("Hello from a function")

hello()

def sapa():
    print("Hello!")

def tanya():
    print("Apa kabar?")

def sakit():
    print("Aduh!")

masukkan = input("Interaksi: ")
if masukkan == "pukul":
    kesakitan()
elif masukkan == "sapa":
    sapa()
elif masukkan == "tanya kabar":
    tanya()

def intro(nama,umur,tinggi):
    print("Halo, perkenalkan aku {}, aku berumur {}, tinggiku adalah {} cm.".format(nama,umur, tinggi))

intro("Aca",20,168)

nama = input("Nama: ")
umur = input("Umur: ")
tinggi = input("Tinggi: ")
intro(nama,umur,tinggi)

#default parameter
def halo(name=""):
    print("Hello " + name)

halo("Aca")

nilai = 6
def nilai2():
    nilai = 10
    print(nilai)

print(nilai)
nilai2()

panjang = 10
lebar = 5

def luas():
    rumus = panjang * lebar
    print(rumus)

luas()