print("Enter cells:")
cells_ = input()
cells = cells_.replace("_"," ")
print("---------")
print("| " + cells[0] + " " + cells[1] + " " + cells[2] + " |")
print("| " + cells[3] + " " + cells[4] + " " + cells[5] + " |")
print("| " + cells[6] + " " + cells[7] + " " + cells[8] + " |")
print("---------")


matriz = [[cells[6], cells[3], cells[0]],
          [cells[7], cells[4], cells[1]],
          [cells[8], cells[5], cells[2]]]





coor = input("Enter the coordinates: ").split()
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

coor_num = []
for x in coor:
    if x in numeros:
        coor_num.append(x)

coor_num_1 = [(int(x) - 1) for x in coor_num]
while len(coor_num) == 0 or coor_num_1[0] > 2 or coor_num_1[1] > 2 or matriz[coor_num_1[0]][coor_num_1[1]] == "X" or matriz[coor_num_1[0]][coor_num_1[1]] == "O":

    if len(coor_num) == 0:
        print("You should enter numbers!")

    elif coor_num_1[0] > 2 or coor_num_1[1] > 2:
        print("Coordinates should be from 1 to 3!")

    elif matriz[coor_num_1[0]][coor_num_1[1]] == "X" or matriz[coor_num_1[0]][coor_num_1[1]] == "O":
        print("This cell is occupied! Choose another one!")

    coor = input("Enter the coordinates: ").split()
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    coor_num = []
    for x in coor:
        if x in numeros:
            coor_num.append(x)

    coor_num_1 = [(int(x) - 1) for x in coor_num]



n = coor_num_1[0]
m = coor_num_1[1]

if  matriz[coor_num_1[0]][coor_num_1[1]] == " " or matriz[coor_num_1[0]][coor_num_1[1]] == " ":
    matriz[coor_num_1[0]][coor_num_1[1]] = "X"

    cellss = [x for x in cells]
    if m == 2:
        cellss[n] = "X"

    elif m == 1:
        cellss[n + m + 2] = "X"

    elif m == 0:
        cellss[n + m + 6] = "X"


    print("---------")
    print("| " + cellss[0] + " " + cellss[1] + " " + cellss[2] + " |")
    print("| " + cellss[3] + " " + cellss[4] + " " + cellss[5] + " |")
    print("| " + cellss[6] + " " + cellss[7] + " " + cellss[8] + " |")
    print("---------")