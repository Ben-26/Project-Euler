




def main():
    matrix = []
    matrix_file = open("0083_matrix.txt", "r")
    for row in matrix_file:
        matrix.append([int(x) for x in row.rstrip().split(",")])  



if __name__ == "__main__":
    main()
