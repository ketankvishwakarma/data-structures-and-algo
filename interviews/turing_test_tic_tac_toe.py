
moves = ["X","O"]
blank = ['_']

board = [[blank[0],blank[0],blank[0]],
        [blank[0],blank[0],blank[0]],
        [blank[0],blank[0],blank[0]]]


def print_board():
    for row in board:
        print("{}, {}, {}".format(row[0],row[1],row[2]))


def begin():
    print("lets begin...")
    all_moves = {"0,0":None,"0,1":None,"0,2":None,
                 "1,0":None,"1,1":None,"1:2":None,
                 "2,0":None,"2,1":None,"2,2":None}
    win_moves = {"0,00,10,2":"WON",
                 "0,0 1,0 2,0,":"won"}
    x_moves = ""
    y_moves = ""
    total_moves = 0
    
    while True:
        print_board()
        current_player = total_moves % len(moves)
        print("X_moves {} o_moves {}".format(x_moves,y_moves))
        print("Enter the position of Player {} (x_position,y_position):".format(moves[current_player]))
        x = input()
        if total_moves==10:
            break
        if x not in all_moves.keys():
            print("{} is not a valid input. \nValid input values are {}".format(x,all_moves.keys()))
            continue
        if all_moves.get(x) is not "TAKEN":
            xx = x.split(",")
            board[int(xx[0])][int(xx[1])] = moves[current_player]
            all_moves[x]="TAKEN"
            total_moves+=1
            if moves[current_player]=='X':
                x_moves=x_moves+x
                if x_moves in win_moves.keys():
                    print("{} won.".format(moves[current_player]))
                    break
            else:
                y_moves=y_moves+x
                if y_moves in win_moves.keys():
                    print("{} won.".format(moves[current_player]))
                    break
        else:
            print("{} is taken try again".format(x))
            continue







if __name__ == "__main__":
    begin()