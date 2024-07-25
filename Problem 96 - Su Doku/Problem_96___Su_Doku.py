from math import ceil
import numpy as np
from test import te

def main():
    row = 0
    
    sudoku_file = open('sudoku.txt', 'r')
    sudoku_matrix = np.full((9, 9), '123456789', dtype='<U9')
    
    for line in sudoku_file:
        line = line.strip()
        if 'Grid' in line:
            if row == 9:
                solve_sudoku(sudoku_matrix)
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
        print(sudoku_matrix)
        #counter += solve_sudoku(sudoku_matrix)[0, 0:3].sum()

def remove_box_candidate(arr, row, col, char):
    box_index = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    row_list = box_index[row // 3][:]
    col_list = box_index[col // 3][:]
    
    row_list.remove(row)
    col_list.remove(col)

    for r in row_list:
        for c in col_list:
            arr[r][c] = arr[r][c].replace(char, '')
    return arr

def update_sudoku_with_unique_candidates(sudoku_matrix):
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

    # Update rows
    for row in range(9):
        update_unique_in_line(sudoku_matrix[row, :])

    # Update columns
    for col in range(9):
        update_unique_in_line(sudoku_matrix[:, col])
      
        
    def extract_box(matrix, row, col):
        # Extracts a 3x3 box starting at (row, col)
        box = []
        for i in range(3):
            for j in range(3):
                box.append(matrix[row + i, col + j])
        return box

    def update_box(matrix, row, col):
        box = extract_box(matrix, row, col)
        update_unique_in_line(box)
        # Place updated box back into the matrix
        idx = 0
        for i in range(3):
            for j in range(3):
                matrix[row + i, col + j] = box[idx]
                idx += 1

        
    # Update 3x3 boxes
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            update_box(sudoku_matrix, row, col)


    return sudoku_matrix
   




def is_sudoku_solved(sudoku_matrix):
    row = 0
    col = 0
    non_unique = True
    while row < 9 and col < 9:
        if len(sudoku_matrix[row][col]) != 1:
            return False
    return True

def solve_sudoku(sudoku_matrix):
    while not is_sudoku_solved(sudoku_matrix):
        sudoku_matrix = update_sudoku_with_unique_candidates(sudoku_matrix)         
        print(sudoku_matrix, "\n")
    return sudoku_matrix


if __name__ == "__main__":
    #main()
    test_funct()
