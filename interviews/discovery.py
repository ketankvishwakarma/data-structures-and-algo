"""
Interviewer: Pratik Ranka
Snake Ladder Game 
"""

import random as rand
board = [0] * 100

 
def roll_dice():
    return rand.randint(1,6)

if __name__=="__main__":
    win = False
    playerOne = {"P1":1}
    playerTwo = {"P2":1}
    players = [playerOne,playerTwo]
    count = 1
    current_player = 0
    current_name = "P1"
    while(not win):
        
        print("Player {} ",players[current_player])
        print("Rolling dice")
        current_position = players[current_player][current_name]
        dice_roll = roll_dice()
        print("dice roll {} ".format(dice_roll))
        current_position = current_position+dice_roll
        players[current_player][current_name] =  current_position
        print("switching players")
        if current_player ==0:
            current_player = 1
            current_name="P2"
        else:
            current_player = 0
            current_name="P1"
        if current_position >= 100:
            win = True 
            print("+++++++++++++++++++++++++")
            print("{} wins".format(players[current_player]) )  
        
        

