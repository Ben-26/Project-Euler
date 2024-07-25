def update_sudoku_candidates(sudoku_matrix):
    sudoku_matrix = clean_candidates(unique_candidates(sudoku_matrix))

def unique_candidates(sudoku_matrix):
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

    # Update rows
    for row in range(9):
        update_unique_in_line(sudoku_matrix[row, :])

    # Update columns
    for col in range(9):
        update_unique_in_line(sudoku_matrix[:, col])
      
    return sudoku_matrix


def clean_candidates(sudoku_matrix):
    for row in range(9):
        