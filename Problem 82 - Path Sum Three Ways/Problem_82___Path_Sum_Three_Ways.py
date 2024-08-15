#TEST
def print_matrix(arr):
    # Determine the maximum length of elements in each column
    col_widths = [max(len(str(row[i])) for row in arr) for i in range(len(arr[0]))]

    # Print each row with elements left-aligned according to the column width
    for row in arr:
        print(" ".join(f"{str(element):<{col_widths[i]}}" for i, element in enumerate(row)))

def main():
    matrix = []
    
    
    matrix_file = open("0082_matrix.txt", "r")
    
    for row in matrix_file:
        matrix.append(row.rstrip().rsplit(","))
    
    
    # Testing
    matrix = [[99, 390, 42, 1007, 55],
     [999, 39, 4, 17, 108],
     [131, 3, 4, 10, 1008],
     [1, 96, 342, 9, 150],
     [630, 803, 746, 2, 111],
     [537, 4, 497, 1, 6],
     [805, 3, 524, 37, 101],
     [5, 3, 24, 37, 101]] 
    
     
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    path_sums = []

if __name__ == "__main__":
    main()

"""
def transpose_matrix(matrix, m, n):
    transpose = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            transpose[j][i] = matrix[i][j]
    return transpose




    #num_rows = len(matrix)
    #num_cols = len(matrix[0])
    matrix = transpose_matrix(matrix, len(matrix), len(matrix[0]))
    print_matrix(matrix)
    
    matrix, num_rows, num_cols = transpose_matrix(matrix, len(matrix), len(matrix[0]))
    #ALLOWED: DOWN, LEFT, RIGHT
 
    #print(f"{len(matrix)} = {num_rows}, {len(matrix[0])} = {num_cols}")

    #print("Matrix")#TEST
    print(matrix)
    print_matrix(matrix)#TEST

    path_sums = [[float("inf") for _ in range(num_cols)] for _ in range(num_rows)]
    
    for i in range(num_cols):
        path_sums[0][i] = int(matrix[0][i])
    
    for row in range(1, num_rows):
        sorted_indexes = sorted(enumerate(path_sums[row]), key = lambda i:i[1])

     
        for idx in range(num_cols):
            col = sorted_indexes[idx][0]
            path_sums[row][col] = min(path_sums[row - 1][col],
                            path_sums[row][col + 1] if col < num_cols - 1 else float("inf"),
                            path_sums[row][col - 1] if col > 0 else float("inf")) + int(matrix[row][col])

        print("\n")
        print(path_sums)        
        #print_matrix(path_sums)
        

"""