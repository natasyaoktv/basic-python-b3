for i in range(2):
    for j in range(3):
        print("i: {}, j:{}".format(i,j))
print("")

#array 3 dimensi
list_angka = [
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]

    ]
]

for i in list_angka:
    for j in i:
        for k in j:
            print(k)
