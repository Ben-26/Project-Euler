
def main():
    matrix = []
    matrix_file = open("0083_matrix.txt", "r")
    for row in matrix_file:
        matrix.append([float('inf')] + [int(x) for x in row.rstrip().split(",")] + [float('inf')]) 
    nrows = len(matrix)  
    f = [float('inf') for _ in range(nrows + 2)]
    matrix = [f] + matrix + [f]

    nrows += 2
    ncols = len(matrix[0])
    
    path_sum = [[float('inf') for _ in range(ncols)] for _ in range(nrows)]
    path_sum[1][1] = matrix[1][1]

    for l in range(1, nrows - 1):
        for _ in range(2):
            row, col = 0, l
        
            while row != col:
                # Col down - cmp above, left and self
                path_sum[row][col] = min(path_sum[row][col - 1] + matrix[row][col],
                                         path_sum[row - 1][col] + matrix[row][col],
                                         path_sum[row][col])
                row += 1

            while col >= 0:
                # Row left - cmp above, right and self
                path_sum[row][col] = min(path_sum[row - 1][col] + matrix[row][col],
                                         path_sum[row][col + 1] + matrix[row][col],
                                         path_sum[row][col])
                col -= 1
           
            while row != col:
                # Row right - cmp above, left and self
                path_sum[row][col] = min(path_sum[row - 1][col] + matrix[row][col],
                                         path_sum[row][col - 1] + matrix[row][col],
                                         path_sum[row][col])
                col += 1

            while row >= 0:
                # Col up - cmp below, left and self
                path_sum[row][col] = min(path_sum[row + 1][col] + matrix[row][col],
                                         path_sum[row][col - 1] + matrix[row][col],
                                         path_sum[row][col])
                row -= 1

    for row in range(1, nrows - 1):
        for col in range(1, ncols - 1):
            path_sum[row][col] = min(path_sum[row - 1][col] + matrix[row][col],
                                     path_sum[row + 1][col] + matrix[row][col],
                                     path_sum[row][col + 1] + matrix[row][col],
                                     path_sum[row][col - 1] + matrix[row][col],
                                     path_sum[row][col])
    print(path_sum[-2][-2])

if __name__ == "__main__":
    main()

