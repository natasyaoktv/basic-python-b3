f = open("file.txt","a")
f.write("Hallo gaes!")
f.close()

f = open("file.txt","a")
f.write("\nHallo juga gaes!")
f.close()

f = open("file.txt", "r")
# print(f.read())
# print(f.read(2))
# print(f.readline())

x = f.readlines()
print(x)
print(x[1])