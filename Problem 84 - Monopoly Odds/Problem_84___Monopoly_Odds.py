from random import randint

def monopoly(n, d):
    def roll_dice(dice):
        return [randint(1, dice) for _ in range(2)]
    
    board = [0] * 40
    
    # Com chest , Go and Jail
    cc = {}
    while len(cc) < 2:
        key = randint(0, 15)
        if key not in cc:
            cc[key] = [0, 10][len(cc)] 

    # Chance card, R = next rail, U = next utility, B = back 3
    ch = {}
    while len(ch) < 10:
        key = randint(0, 15)
        if key not in ch:
            ch[key] = [0, 10, 11, 24, 39, 5, 'R', 'R', 'U', 'B'][len(ch)] 
    
    cc_counter = 0
    ch_counter = 0
    double_counter = 0
    pos = 0
    turns = 0
    moved = False
    
    while turns < n: # Turns
        roll = roll_dice(d)
        if roll[0] == roll[1]: # Double check
            double_counter += 1
        else:
            double_counter = 0
            
        if double_counter == 3: # Three doubles
            double_counter = 0
            pos = 10
            moved = True
        else:
            pos = (pos + sum(roll)) % 40 
            board[pos] += 1
            
            if pos in [2, 17, 34]: # com chest
                if cc_counter % 16 in cc:
                    pos = cc[cc_counter]
                    moved = True
                cc_counter = (cc_counter + 1) % 16
                
            elif pos in [8, 22, 36]: # chance
                if ch_counter % 16 in ch:
                    if ch[ch_counter] == 'R':
                        pos = 15 if pos == 8 else (25 if pos == 22 else 5)
                    elif ch[ch_counter] == 'U':
                        pos = 12 if pos == 8 or pos == 36 else 28
                    elif ch[ch_counter] == 'B':
                        pos -= 3
                    else:
                        pos = ch[ch_counter]
                    moved = True
                ch_counter = (ch_counter + 1) % 16
                
            elif pos == 30:
                pos = 10
                moved += 1
                
        if moved:
            board[pos] += 1
            moved = False
        turns += 1  
    return board

def main():
    board = [0] * 40
    for i in range(30): # Num games
        for j, visits in enumerate(monopoly(2**17, 4)):
            board[j] += visits

    max_str = ""
    for n in reversed(sorted(board)[-3:]):
        idx = board.index(n)
        if idx < 10:
            max_str += "0" + str(idx)
        else:
            max_str += str(idx)          
    print(max_str)

if __name__ == "__main__":
    main()
