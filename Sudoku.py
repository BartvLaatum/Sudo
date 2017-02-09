w = 9
h = 9
sudoku = [[0 for x in range(w)] for y in range(h)]
sudokuFile = open("puzzle1.sudoku", "r")

for line in sudokuFile:
    print (line)
    line = line.replace(',', '')
    print (line)


for x in range(len(sudoku))
