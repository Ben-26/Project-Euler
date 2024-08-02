import random

def three_most_popular_squares(dice, turns):
    action_indexes = [2, 7, 17, 22, 30, 33, 36]
    # 1 : Chance card
    # 2 : Community chest
    # 3 : Go to Jail

    board = {}
    for i, square in enumerate(40):
        board[i] = {"Visits" : 0, "Actions" : int(i in action_indexes)}
        
    pos = 0 
    
    def roll_dice(dice):
        return [random.randint(1, dice) for _ in range(2)]


    for i in range(turns):
        pos += sum(roll_dice())
        pos %= 40
        board[pos]["Visited"] += 1
        if board[pos]["Actions"] == 0:
            pass
        elif board[pos]["Actions"] == 1:
            #chance card
            pass
        elif board[pos]["Actions"] == 2:
            pass
        elif board[pos]["Actions"] == 3:
            pos = 10
            board[pos]["Visited"] += 1
            
            



def main():
    pass

if __name__ == "__main__":
    main()
