def board(x):
    print(
          "", x[0]," ",x[1]," ",x[2],"\n",
          x[3]," ",x[4]," ",x[5],"\n",
          x[6]," ",x[7]," ",x[8],"\n",
           )

def checker(x): 

    if x[0] == "x" and x[1] == "x" and x[2] == "x":
            return 1
    elif x[0] == "x" and x[4] == "x" and x[8] == "x":
        return 1
    elif x[2] == "x" and x[4] == "x" and x[6] == "x":
        return 1
    elif x[3] == "x" and x[4] == "x" and x[5] == "x":
        return 1
    elif x[6] == "x" and x[7] == "x" and x[8] == "x":
        return 1
    elif x[6] == "x" and x[7] == "x" and x[8] == "x":
        return 1

    if x[0] == "o" and x[1] == "o" and x[2] == "o":
            return 2
    elif x[0] == "o" and x[4] == "o" and x[8] == "o":
        return 2
    elif x[2] == "o" and x[4] == "o" and x[6] == "o":
        return 2
    elif x[3] == "o" and x[4] == "o" and x[5] == "o":
        return 2
    elif x[6] == "o" and x[7] == "o" and x[8] == "o":
        return 2
    elif x[6] == "o" and x[7] == "o" and x[8] == "o":
        return 2

x = ["1" , "2" , "3" , "4" , "5" , "6", "7" , "8" , "9"]
i = 0
while 1:
    board(x)
    p1 = int(input("Player 1 -> "))
    x[p1 - 1] = "x"
    board(x)
    che = checker(x)
    if che == 1: 
            print("x  won");
            break;
    p2 = int(input("Player 2 -> "))
    x[p2 - 1] = "o"
    board(x)
    che = checker(x)
    if che == 2: 
            print("y  won");
            break;

    i += 1
    if i == 8:
        print("tie")
        break;

