Brainfuck-Interpreter
=====================

A simple Brainfuck interpter written in python


EXAMPLES

# Copies cell #1 to Cell #2 and prints the ASCII value of cell #2
program = '++++++ [ > ++++++++++ < - ] > +++++ .'

# Reads a input character and copies to cell #2
program = ', [ > + < - ] > .'

 # Reads two input characters, multiply them, stores the result on cell #3
program = ',>,< [ > [ >+ >+ << -] >> [- << + >>] <<< -] >>'

# Makes the program run out of memory
program = '+[>+]'