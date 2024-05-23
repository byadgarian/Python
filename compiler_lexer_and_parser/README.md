# Project

Compiler grammer parser and lexical analyzer program

## Author

Author: Brian Y. Copyright © 2022. All rights reserved. <br/>
E-Mail: ***

## Execute

Run the following command

    python main.py

    or

    python3 main.py

## Output

Reading and analyzing the code file using lexical analyzer... <br/>

Token:  identifier            Lexeme:  a <br/>
Token:  assignOp            Lexeme:  =   <br/>
Token:  identifier            Lexeme:  b <br/>
Token:  addOp            Lexeme:  +      <br/>
Token:  identifier            Lexeme:  c <br/>
Token:  addOp            Lexeme:  +      <br/>
Token:  identifier            Lexeme:  d <br/>
Token:  semicolon            Lexeme:  ;  <br/>

End of file reached. Parsing completed. <br/>

Analyzing completed. Token Stream = ['identifier', 'assignOp', 'identifier', 'addOp', 'identifier', 'addOp', 'identifier'] <br/>

Parsing the token stream... <br/>

Stack = [0] ^^^ Token Stream = ['identifier', 'assignOp', 'identifier', 'addOp', 'identifier', 'addOp', 'identifier', '$'] ^^^ Table Entry = S3 ^^^ Action = Shift; push identifier ; push 3 <br/>
Stack = [0, 'identifier', 3] ^^^ Token Stream = ['assignOp', 'identifier', 'addOp', 'identifier', 'addOp', 'identifier', '$'] ^^^ Table Entry = R4 ^^^ Action = Reduce; E -> identifier <br/>
Stack = [0, 'E', 2] ^^^ Token Stream = ['assignOp', 'identifier', 'addOp', 'identifier', 'addOp', 'identifier', '$'] ^^^ Table Entry = S5 ^^^ Action = Shift; push assignOp ; push 5 <br/>
Stack = [0, 'E', 2, 'assignOp', 5] ^^^ Token Stream = ['identifier', 'addOp', 'identifier', 'addOp', 'identifier', '$'] ^^^ Table Entry = S8 ^^^ Action = Shift; push identifier ; push 8 <br/>
Stack = [0, 'E', 2, 'assignOp', 5, 'identifier', 8] ^^^ Token Stream = ['addOp', 'identifier', 'addOp', 'identifier', '$'] ^^^ Table Entry = R4 ^^^ Action = Reduce; E -> identifier <br/>
Stack = [0, 'E', 2, 'assignOp', 5, 'E', 7] ^^^ Token Stream = ['addOp', 'identifier', 'addOp', 'identifier', '$'] ^^^ Table Entry = S9 ^^^ Action = Shift; push addOp ; push 9 <br/>
Stack = [0, 'E', 2, 'assignOp', 5, 'E', 7, 'addOp', 9] ^^^ Token Stream = ['identifier', 'addOp', 'identifier', '$'] ^^^ Table Entry = S10 ^^^ Action = Shift; push identifier ; push 10 <br/>
Stack = [0, 'E', 2, 'assignOp', 5, 'E', 7, 'addOp', 9, 'identifier', 10] ^^^ Token Stream = ['addOp', 'identifier', '$'] ^^^ Table Entry = R3 ^^^ Action = Reduce; E -> E + identifier <br/>
Stack = [0, 'E', 2, 'assignOp', 5, 'E', 7] ^^^ Token Stream = ['addOp', 'identifier', '$'] ^^^ Table Entry = S9 ^^^ Action = Shift; push addOp ; push 9 <br/>
Stack = [0, 'E', 2, 'assignOp', 5, 'E', 7, 'addOp', 9] ^^^ Token Stream = ['identifier', '$'] ^^^ Table Entry = S10 ^^^ Action = Shift; push identifier ; push 10 <br/>
Stack = [0, 'E', 2, 'assignOp', 5, 'E', 7, 'addOp', 9, 'identifier', 10] ^^^ Token Stream = ['$'] ^^^ Table Entry = R3 ^^^ Action = Reduce; E -> E + identifier <br/>
Stack = [0, 'E', 2, 'assignOp', 5, 'E', 7] ^^^ Token Stream = ['$'] ^^^ Table Entry = R1 ^^^ Action = Reduce; S -> E = E <br/>
Stack = [0, 'S', 1] ^^^ Token Stream = ['$'] ^^^ Table Entry = ACCT <br/>

Token stream is valid. <br/>

Program successfully analyzed and parsed the code. <br/>