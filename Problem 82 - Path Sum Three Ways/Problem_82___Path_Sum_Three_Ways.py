
def main():
    matrix = []
    matrix_file = open("0082_matrix.txt", "r")
    for row in matrix_file:
        matrix.append([int(x) for x in row.rstrip().split(",")])  

    nrows = len(matrix)
    ncols = len(matrix[0])

    path_sum = [[(matrix[row][0] if col == 0 else 0) for col in range(ncols)] for row in range(nrows)]
    
    for col in range(1, ncols):
        path_sum[0][col] = matrix[0][col] + path_sum[0][col - 1]
        
        for _ in range(2):
            for row in range(nrows):
                path_sum[row][col] = matrix[row][col] + min(path_sum[row - 1][col], path_sum[row][col - 1])
            for row in range(nrows - 2, -1, -1):
                path_sum[row][col] = min(path_sum[row + 1][col] + matrix[row][col], path_sum[row][col])

    print(min([path_sum[i][ncols - 1] for i in range(nrows)]))

if __name__ == "__main__":
    main()
