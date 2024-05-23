import csv

state_table = []
token_table = []
reserved_table = []
lexeme = ''
terminate = False
char_found = False
line_number = 0

answer = input('Would you like to proivde a path to the states csv file? Enter \'y\' for yes, anything else to use the local diroctory file.\n')
if answer == 'y' or answer == 'Y':
    path = input('Please enter the path to the states csv file:\n')
    with open(path, 'r') as state_csv_file:
        state_container = csv.reader(state_csv_file)
        for state_row in state_container:
            state_table.append(state_row)
else:
    with open("state.csv", 'r') as state_csv_file:
        state_container = csv.reader(state_csv_file)
        for state_row in state_container:
            state_table.append(state_row)

answer = input('Would you like to proivde a path to the tokens csv file? Enter \'y\' for yes, anything else to use the local diroctory file.\n')
if answer == 'y' or answer == 'Y':
    path = input('Please enter the path to the tokens csv file:\n')
    with open(path, 'r') as token_csv_file:
        token_container = csv.reader(token_csv_file)
        for token_row in token_container:
            token_table.append(token_row)
else:
    with open('token.csv', 'r') as token_csv_file:
        token_container = csv.reader(token_csv_file)
        for token_row in token_container:
            token_table.append(token_row)

answer = input('Would you like to proivde a path to the reserved words csv file? Enter \'y\' for yes, anything else to use the local diroctory file.\n')
if answer == 'y' or answer == 'Y':
    path = input('Please enter the path to the reserved words csv file:\n')
    with open(path, 'r') as reserved_csv_file:
        reserved_container = csv.reader(reserved_csv_file)
        for reserved_row in reserved_container:
            reserved_table.append(reserved_row)
else:
    with open('reserved.csv', 'r') as reserved_csv_file:
        reserved_container = csv.reader(reserved_csv_file)
        for reserved_row in reserved_container:
            reserved_table.append(reserved_row)

answer = input('Would you like to proivde a path to the source code text file? Enter \'y\' for yes, anything else to use the local diroctory file.\n')
if answer == 'y' or answer == 'Y':
    path = input('Please enter the path to the source code text file:\n')
else:
    path = 'code.txt'

with open(path, 'r') as code_txt_file:
    state = 1
    for line in code_txt_file:
        if terminate == True:
            break

        length = len(line)
        c = 0

        if line_number == 0:
            answer = input('Would like to get the next token? Enter \'y\' to proceed, anything else to terminate.\n')
            if answer == 'y' or answer == 'Y':
                terminate = False
            else:
                terminate = True

        while c != length and terminate == False:
            char = line[c]
            c = c + 1
            
            if hex(ord(char)) != '0xa' and hex(ord(char)) != '0x0a' and hex(ord(char)) != '0x0d' and hex(ord(char)) != '0x20' and hex(ord(char)) != '0x9' and hex(ord(char)) != '0x09': #add '0x9
                lexeme = lexeme + char
            
            for j in range(0, len(state_table[0])):
                if state_table[0][j] == char or state_table[0][j] == hex(ord(char)):
                    char_found = True
                    if state_table[state][j]:
                        state = int(state_table[state][j]) + 1
                    else:
                        print('Error: Unacceptable token. Check line number', line_number + 1, ', character number', c - 1, '(char =', char, ').')
                        lexeme = ''
                        state = 1
            
            if char_found == False:
                print('Error: Illegal character found. Check line number', line_number + 1, ', character number', c - 1, '(char =', char, ').')
                lexeme = ''
                state = 1
            else:
                char_found = False
            
            if token_table[state][1]:
                if token_table[state][1] == 'identifier' or token_table[state][1] == 'assignOp' or token_table[state][1] == 'comparator' and char != '=' or token_table[state][1] == 'addOp' or token_table[state][1] == 'multOp' or token_table[state][1] == 'intLiteral' and char != 'u' and char != 'l' and char != 'U' and char != 'L' or token_table[state][1] == 'floatLiteral' or token_table[state][1] == 'logicalNot':
                    c = c - 1
                    if hex(ord(char)) != '0xa' and hex(ord(char)) != '0x0a' and  hex(ord(char)) != '0x0d' and hex(ord(char)) != '0x20' and hex(ord(char)) != '0x9' and hex(ord(char)) != '0x09':
                        lexeme = lexeme[:-1]

                token = token_table[state][1]
                for l in range(0, len(reserved_table)):
                    if lexeme == reserved_table[l][0]:
                        token = lexeme

                if token_table[state][1] == 'comment':
                    print('Comment was ignored.')
                else:
                    print('Token: ', token, '          ', 'Lexeme: ', lexeme)
                state = 1
                lexeme = ''

                answer = input('Would like to get the next token? Enter \'y\' to proceed, anything else to terminate.\n')
                if answer == 'y' or answer == 'Y':
                    terminate = False
                else:
                    terminate = True
            
        line_number = line_number + 1

    if token_table[state][1] or state == 1:
        print('End of file reached. Parsing completed.')
    else:
        print('Error: End of file reached unexpectedly. Not in an accepting state. Check line number', line_number, ', character number', c - 1, '(char =', char, ').')