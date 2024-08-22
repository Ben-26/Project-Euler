import numpy as np

def main():
    with open("0082_matrix.txt", "r") as matrix_file:
        matrix = np.array([[int(char) for char in row.rstrip().rsplit(",")] for row in matrix_file])
    
    print(matrix)


if __name__ == "__main__":
    main()

    """
        # Testing
    matrix = [[99, 390, 42, 1007, 55],
     [999, 39, 4, 17, 108],
     [131, 3, 4, 10, 1008],
     [1, 96, 342, 9, 150],
     [630, 803, 746, 2, 111],
     [537, 4, 497, 1, 6],
     [805, 3, 524, 37, 101],
     [5, 3, 24, 37, 101]] 
    

    
    """