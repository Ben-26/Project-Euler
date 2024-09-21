def main():
    network = []
    with open("0107_network.txt", "r") as network_file:
        for line in network_file:
            network.append([int(x) if x != "-" else 0 for x in line.rstrip().split(",")])

    wO = sum([sum(row) for row in network]) // 2
    wM = float("inf")
    
    # Want one element in each row ? 


    

if __name__ == "__main__":
    #main()

    before = [[ 0, 16, 12, 21,  0,  0,  0],
              [16,  0,  0, 17, 20,  0,  0],
              [12,  0,  0, 28,  0, 31,  0],
              [21, 17, 28,  0, 18, 19, 23],
              [ 0, 20,  0, 18,  0,  0, 11],
              [ 0,  0, 31, 19,  0,  0, 27],
              [ 0,  0,  0, 23, 11, 27,  0]]

    after = [[ 0, 16, 12,  0,  0,  0,  0],
             [16,  0,  0, 17,  0,  0,  0],
             [12,  0,  0,  0,  0,  0,  0],
             [ 0, 17,  0,  0, 18, 19,  0],
             [ 0,  0,  0, 18,  0,  0, 11],
             [ 0,  0,  0, 19,  0,  0,  0],
             [ 0,  0,  0,  0, 11,  0,  0]]