# Sudoku Solver using SAT
## Requirements
- Ensure that you are using a Linux command line interface
- Have minisat and git installed
## Note:
- The Sudoku text file can be given in any format.
- The spaces with no numbers can be any character, even zero's!


## Setup
1. Clone this repo using:

    ```bash
     # Example
     git clone https://github.com/raastinn/sudoku-solver
   ```
2. Run sudoku2sat with any Sudoku file, which will produce a file called puzzle.cnf with all the clauses:
    ```bash
     # Example
     python3 sudoku2sat.py sampleSudoku.txt
   ```
3. Run minisat and output the result into a file
    ```bash
     # Example
     minisat puzzle.cnf assignments.txt
   ```
4. Run sat2sudoku puzzle.cnf with the file containing the clauses created by minisat
    ```bash
     # Example
     python3 sat2sudoku.py assignments.txt
   ```
5. Now you have a file called solution.txt which solves the Sudoku for you!
