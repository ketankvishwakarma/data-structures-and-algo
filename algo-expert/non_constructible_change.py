"""
  Given an array of positive integers representing the values of coins in your
  possession, write a function that returns the minimum amount of change (the
  minimum sum of money) that you can not create. 
  
  The given coins can have any positive integer value and aren't necessarily unique (i.e., you can have
  multiple coins of the same value).
"""

def change_we_canot_generate(coins):
    coins.sort()
    current_change = 0
    if len(coins) ==0:
        return 1
    if coins[0]>1:
        return 1
    for coin in coins:
        if coin > current_change+1:
            return current_change+1
        else:
            current_change+=coin
    return current_change+1

if __name__=="__main__":
    print(change_we_canot_generate([1,1,3,4]))
    print(change_we_canot_generate([1,1,4]))