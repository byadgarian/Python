# This is the lexical analyzer file containing the Lexer class
# Upon successful executtion, the analize_code_chars() function tokenizes the code and returns a list called token_stream

import csv

class Lexer:

    # lexer function
    def analize_code_chars(code_file_path):

        # declare variables and empty lists
        state_table = []
        token_table = []
        reserved_table = []
        token_stream = []
        lexeme = ''
        char_found = False
        line_number = 0

        # load data from csv files into lists
        state_table_csv = open('state_table.csv')
        state_table_data = csv.reader(state_table_csv)
        state_table = list(state_table_data)
        state_table_csv.close()

        token_table_csv = open('token_table.csv')
        token_table_data = csv.reader(token_table_csv)
        token_table = list(token_table_data)
        token_table_csv.close()

        reserved_table_csv = open('reserved_table.csv')
        reserved_table_data = csv.reader(reserved_table_csv)
        reserved_table = list(reserved_table_data)
        reserved_table_csv.close()

        # open code file
        with open(code_file_path, 'r') as code_txt_file:
            state = 1

            # analize code file line by line, char by char
            for line in code_txt_file:
                length = len(line)
                c = 0

                # consume chars until all chars in a single line are consumed
                while c != length:
                    char = line[c]
                    c = c + 1
                    
                    # add char to lexeme unless it is a space, tab or line-break
                    if hex(ord(char)) != '0xa' and hex(ord(char)) != '0x0a' and hex(ord(char)) != '0x0d' and hex(ord(char)) != '0x20' and hex(ord(char)) != '0x9' and hex(ord(char)) != '0x09':
                        lexeme = lexeme + char
                    
                    # find char in states table, then find the next state or return error if state is not found
                    for j in range(0, len(state_table[0])):
                        if state_table[0][j] == char or state_table[0][j] == hex(ord(char)):
                            char_found = True
                            if state_table[state][j]:
                                state = int(state_table[state][j]) + 1
                            else:
                                print('Error: Unacceptable token. Check line number', line_number + 1, ', character number', c - 1, '(char =', char, ').')
                                lexeme = ''
                                state = 1
                    
                    # return error if char is illegal
                    if char_found == False:
                        print('Error: Illegal character found. Check line number', line_number + 1, ', character number', c - 1, '(char =', char, ').')
                        lexeme = ''
                        state = 1
                    else:
                        char_found = False
                    
                    # if token is found, then handle special cases, reserved keywords and comments, then print and store token
                    if token_table[state][1]:

                        #handle special cases
                        if token_table[state][1] == 'identifier' or token_table[state][1] == 'assignOp' or token_table[state][1] == 'comparator' and char != '=' or token_table[state][1] == 'addOp' or token_table[state][1] == 'multOp' or token_table[state][1] == 'intLiteral' and char != 'u' and char != 'l' and char != 'U' and char != 'L' or token_table[state][1] == 'floatLiteral' or token_table[state][1] == 'logicalNot':
                            c = c - 1

                            # eliminate space, tab or line-break from lexeme
                            if hex(ord(char)) != '0xa' and hex(ord(char)) != '0x0a' and  hex(ord(char)) != '0x0d' and hex(ord(char)) != '0x20' and hex(ord(char)) != '0x9' and hex(ord(char)) != '0x09':
                                lexeme = lexeme[:-1]
                        
                        # handle reserved keywords
                        token = token_table[state][1]
                        for l in range(0, len(reserved_table)):
                            if lexeme == reserved_table[l][0]:
                                token = lexeme

                        # handle comments and print and store token
                        if token_table[state][1] == 'comment':
                            print('Comment was ignored.')
                        else:
                            print('Token: ', token, '          ', 'Lexeme: ', lexeme)
                            token_stream.append(token)
                        state = 1
                        lexeme = ''
                    
                # go to the next line
                line_number = line_number + 1

            # eliminate ';' from token stream
            token_stream = token_stream[:-1]
            
            # print success/failure message
            if token_table[state][1] or state == 1:
                print('\nEnd of file reached. Parsing completed.')
            else:
                print('Error: End of file reached unexpectedly. Not in an accepting state. Check line number', line_number, ', character number', c - 1, '(char =', char, ').')

            # close code file
            code_txt_file.close()
        
        return token_stream