from math import ceil
from re import L
import numpy as np

def main():
    row = 0
    counter = 0
    
    sudoku_file = open('sudoku.txt', 'r')
    sudoku_matrix = np.full((9, 9), '123456789', dtype='<U9')
    
    for line in sudoku_file:
        line = line.strip()
        if 'Grid' in line:
            row = 0
            sudoku_matrix = np.full((9, 9), '123456789', dtype='<U9')
        else:
            for col, char in enumerate(line):
                if char != '0':
                    # Remove the digit from the row and column 
                    for i in range(9):
                        if char in sudoku_matrix[row, i]:
                            sudoku_matrix[row, i] = sudoku_matrix[row, i].replace(char, '')
                        if char in sudoku_matrix[i, col]:
                            sudoku_matrix[i, col] = sudoku_matrix[i, col].replace(char, '') 
                    sudoku_matrix = remove_box_candidate(sudoku_matrix, row, col, char)

                    sudoku_matrix[row, col] = char
            row += 1
            
        if row == 9:
            print(sudoku_matrix, "\n")
            sudoku_matrix = update_unique_candidates(sudoku_matrix)
            print(sudoku_matrix, "\n")
            sudoku_matrix = clean_candidates(sudoku_matrix)
            print(sudoku_matrix, "\n")
            #]counter += solve_sudoku(sudoku_matrix)[0, 0:3].sum()

def remove_box_candidate(sudoku_matrix, row, col, char):
    box_index = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    row_list = box_index[row // 3][:]
    col_list = box_index[col // 3][:]
    
    row_list.remove(row)
    col_list.remove(col)

    for r in row_list:
        for c in col_list:
            sudoku_matrix[r][c] = sudoku_matrix[r][c].replace(char, '')
    return sudoku_matrix

def update_unique_candidates(sudoku_matrix):
    # Checks if there is only one instance of the number in the row
    def update_unique_in_line(line):
        char_count = {}
        for idx, cand in enumerate(line):
            for char in cand:
                if char in char_count:
                    char_count[char]['count'] += 1
                else:
                    char_count[char] = {'count': 1, 'index': idx}
        for char, info in char_count.items():
            if info['count'] == 1:
                line[info['index']] = char
                # TODO add a function that removes this character from all the candidates on the line
     
    # Update rows
    for row in range(9):
        update_unique_in_line(sudoku_matrix[row, :])

    # Update columns
    for col in range(9):
        update_unique_in_line(sudoku_matrix[:, col])
      
    return sudoku_matrix

def clean_candidates(sudoku_matrix):
    def clean_line(line, row):
        for col, char in enumerate(line):
            for i in range(9):
                if char in sudoku_matrix[row, i]:
                    sudoku_matrix[row, i] = sudoku_matrix[row, i].replace(char, '')
                if char in sudoku_matrix[i, col]:
                    sudoku_matrix[i, col] = sudoku_matrix[i, col].replace(char, '') 
                    #sudoku_matrix = remove_box_candidate(sudoku_matrix, row, col, char)
    
    for row in range(9):
        clean_line(sudoku_matrix[row, :], row)

    return sudoku_matrix

def is_sudoku_solved(sudoku_matrix):
    # Dictionary to store rows and columns
    row_dict = {i: [] for i in range(9)}
    col_dict = {i: [] for i in range(9)}
    
    # Iterate over the matrix to populate the dictionary
    for row in range(9):
        for col in range(9):
            num = sudoku_matrix[row][col]
            row_dict[row].append(num)
            col_dict[col].append(num)
    
    # Define the target set of numbers
    target_set = set(range(1, 10))
    
    # Check if each row and column contains exactly the numbers 1 through 9
    for i in range(9):
        if set(row_dict[i]) != target_set:
            return False
        if set(col_dict[i]) != target_set:
            return False
    
    return True

def solve_sudoku(sudoku_matrix):
    while not is_sudoku_solved(sudoku_matrix):
        sudoku_matrix = update_unique_candidates(sudoku_matrix)
        print(sudoku_matrix, "\n")
    return sudoku_matrix


if __name__ == "__main__":
    main()
    
