# Format of the Game Board
def print_board(a):
    print("",a[1]," │",a[2]," │ ",a[3]," ")
    print("────┼────┼────")
    print("",a[4]," │",a[5]," │ ",a[6]," ")
    print("────┼────┼────")
    print("",a[7]," │",a[8]," │ ",a[9]," ")

# Instruction of game
def print_instructions():
    print("\n----------- WELCOME TO TIC TAC TOE ------------\n\n")
    print_board(pos)
    print()

    players[0] = input("Player 1 : ")
    players[1] = input("Player 2 : ")

    print("\n-------- Instructions ---------")
    print("->",players[0],"you will using X")
    print("->",players[1],"you will using 0")
    print("-> Turn starts from",players[0])
    print("-> Potisions are like :-")
    print("  1 │  2 │ 3  ")
    print("────┼────┼────")
    print("  4 │ 5  │ 6  ")
    print("────┼────┼────")
    print("  7 │ 8  │ 9  ")
    print("-> Press S to Start the Game")
    flag = input()
    return flag

# To Initialise the game
def startgame():
    turn = 0
    for i in range(9):
        if turn % 2 == 0:
            print("\nIts Your Turn",players[0])
            p = int(input("Please Enter postion : "))
            v = 'x'
            pos[p] = v
            print_board(pos)
            winner = checkwin(v)
            if winner is "Nobody":
                turn = 1
                continue
            else:
                print("\n\nHurray !!,",players[0],"You Won XD I Love You")
                break
        else:
            print("\nIts Your Turn",players[1])
            p = int(input("Please Enter Postion : "))
            v = '0'
            pos[p] = v
            print_board(pos)
            winner = checkwin(v)
            if winner is "Nobody":
                turn = 0
                continue
            else:
                print("\n\nHurray !!,",players[1],"You Won XD")
                break
    else:
        print("\n\nGame is Draw")

# heck for winner
def checkwin(v):
    for i in winning_conditions:
        if (pos[i[0]], pos[i[1]], pos[i[2]]) == (v,v,v):
            winner = players[0]
            break
        elif (pos[i[0]], pos[i[1]], pos[i[2]]) == (v,v,v):
            winner = players[1]
            break
    else:
        winner = "Nobody"
    return winner

# Game
pos = ['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
players = ['','']
winning_conditions = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
flag = print_instructions()
if flag == 's' or flag == 'S':
    startgame()
else:
    print("Invalid Entry")
