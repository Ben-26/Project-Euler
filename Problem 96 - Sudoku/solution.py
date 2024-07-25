from update_sudoku_candidates import update_sudoku_candidates

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
        sudoku_matrix = update_sudoku_candidates(sudoku_matrix)
    return sudoku_matrix
