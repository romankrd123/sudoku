from itertools import product

def solve_sudoku(puzzle):
    for(row, col) in product(range(0, 9), repeat=2):
        if puzzle[row][col] == 0:
            for num in range(1, 10):
                allowed = True
                for i in range(0, 9):
                    if(puzzle[i][col] == num) or (puzzle[row][i] == num):
                        allowed = False; break
                for(i,j) in product(range(0, 3), repeat=2):
                    if puzzle[row-row%3+i][col-col%3+j] == num:
                        allowed = False; break
                if allowed:
                    puzzle[row][col] = num
                    if trial := solve_sudoku(puzzle):
                        return trial
                    else:
                        puzzle[row][col] = 0
            return False
    return puzzle
def print_sudoku(puzzle):
    puzzle = [['*' if num == 0 else num for num in row] for row in puzzle]
    print()
    for row in range(0, 9):
        if((row%3 == 0) and (row != 0)):
            print('-'*29)
        for col in range(0, 9):
            if((col%3 == 0) and (col != 0)):
                print('|', end = '')
            print('', puzzle[row][col], '', end = '')
        print()
    print()
if __name__ == '__main__':
    ######################################################
    ###       В переменной puzzle надо вставить        ###
    ###           цифру из Вашего судоку,              ###
    ###      если она не вставленна, то поставте 0     ###
    ###                                                ###
    ######################################################
    puzzle = [
        [0, 0, 1, 0, 0, 0, 2, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 4, 0],
        [5, 0, 0, 0, 3, 0, 0, 0, 6],
        [0, 0, 0, 1, 0, 7, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 9, 0, 2, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 6, 0, 0, 5, 0, 0, 3, 0],
        [0, 0, 2, 0, 0, 0, 7, 0, 0]
    ]
print_sudoku(puzzle)
solution = solve_sudoku(puzzle)
print_sudoku(solution)