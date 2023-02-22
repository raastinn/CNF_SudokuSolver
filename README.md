# Sudoku Solver using SAT
## Requirements
- Ensure that you are using a Linux command line interface
- Have minisat and git installed
## Setup
1. Clone this repo using:

    ```bash
     git clone https://github.com/raastinn/sudoku-solver
   ```
2. Run sudoku2sat with any Sudoku file, which will produce a file called puzzle.cnf with all the clauses
3. Run minisat and output the result into a file
4. Run sat2sudoku puzzle.cnf with the file containing the clauses created by minisat
5. Now you have a file called solution.txt which solves the Sudoku for you!
