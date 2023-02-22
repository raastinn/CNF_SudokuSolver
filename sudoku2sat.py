#! /usr/bin/env python3
import sys
import re

if __name__ == '__main__':

    def var(row, column, value):
        return 81*(row-1)+9*(column-1)+(value-1)+1

    # Read sudoku and add the given clues as clauses
    clauses = []
    fileName = sys.argv[1]
    with open(fileName, "r") as f:
            sudoku = re.sub(r"[\n\t\s]*", "", f.read()) #remove spaces, tabs and new lines
    for row in range(9):
        for col in range(9):
            curr_char = sudoku[row*9 + col]
            if curr_char.isnumeric() and int(curr_char): # if number and not zero
                clauses.append([var(row+1, col+1, int(curr_char))])
    
    # Every cell contains at least one number
    for row in range(1, 10):
        for column in range(1, 10):
            clauses.append([var(row, column, value) for value in range(1, 10)])

    # Each number appears at most once in every row
    for i in range(1, 10):
        for k in range(1, 10):
            for j in range(1, 9):
                for l in range(j+1, 10):
                    clauses.append([-var(i, j, k), -var(i, l, k)])

    # Each number appears at most once in every column
    for j in range(1, 10):
        for k in range(1, 10):
            for i in range(1, 9):
                for l in range(i+1, 10):
                    clauses.append([-var(i, j, k), -var(l, j, k)])

    # Each number appears at most one in every 3x3 sub-grid
    for k in range(1, 10):
        for a in range(0, 3):
            for b in range(0, 3):
                for u in range(1, 4):
                    for v in range(1, 3):
                        for w in range(v+1, 4):
                            clauses.append([-var(3*a+u,3*b+v,k), -var(3*a+u,3*b+w,k)])
                for u in range(1, 3):
                    for v in range(1, 4):
                        for w in range(u+1, 4):
                            for t in range(1, 4):
                                clauses.append([-var(3*a+u,3*b+v,k), -var(3*a+w,3*b+t, k)])

    # Create the CNF file for minisat
    f = open("puzzle.cnf", "w+")

    # Print the header line
    f.write("p cnf %d %d\n" % (729, len(clauses)))

    # Print the clauses
    for c in clauses:
        f.write(" ".join([str(l) for l in c])+" 0\n")

    # Close file created
    f.close()
