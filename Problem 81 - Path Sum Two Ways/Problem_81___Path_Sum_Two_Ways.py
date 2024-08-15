def main():
    matrix = []
    matrix_file = open("0081_matrix.txt", "r")
    
    for row in matrix_file:
        matrix.append(row.rstrip().rsplit(","))
   
    path_sums = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))] 
    path_sums[0][0] = int(matrix[0][0])

    for i in range(1, len(matrix)):
        path_sums[i][0] = path_sums[i - 1][0] + int(matrix[i][0]) 
        path_sums[0][i] = path_sums[0][i - 1] + int(matrix[0][i])
        
    for i in range(1, len(matrix)):
        for j in range(i, len(matrix)):
            path_sums[i][j] = min(path_sums[i - 1][j], path_sums[i][j - 1]) + int(matrix[i][j])
            path_sums[j][i] = min(path_sums[j - 1][i], path_sums[j][i - 1]) + int(matrix[j][i])
       
    print(path_sums[-1][-1])
       
if __name__ == "__main__":
    main()
