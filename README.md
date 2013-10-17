Brainfuck-Interpreter
=====================


A simple Brainfuck interpreter written in python

## Code Example

The program simply reads brainfuck programs and output the result(if there is any) and/or the cells that were created throughout the program(if specified)

## Installation

Simply call ```python BFInterpreter.py 'Your_Program_Here'```.
Append --enable-output to output the contents of every cell in the end of the program

## Tests
A couple of examples goes below:

Copies cell #1 to Cell #2 and prints the ASCII value of cell #2
```python BFInterpreter.py '++++++ [ > ++++++++++ < - ] > +++++ .'```

Reads a input character and copies to cell #2
```python BFInterpreter.py ', [ > + < - ] > .'```

Reads two input characters, multiply them, stores the result on cell #3
```python BFInterpreter.py ',>,< [ > [ >+ >+ << -] >> [- << + >>] <<< -] >>'```

Makes the program run out of memory
```python BFInterpreter.py '+[>+]'```

## License

GNU LGPL License