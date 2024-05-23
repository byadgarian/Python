# This is the parser file containing the Parser class
# Upon successful execution, the parse_token_stream() function returns the parsing status (successful = 1, failed = 0)

import csv

class Parser:

    # parser function
    def parse_token_stream(token_stream):

        # load data from csv file into a list
        parser_table_csv = open('parser_table.csv')
        parser_table_data = csv.reader(parser_table_csv)
        parser_table = list(parser_table_data)
        parser_table_csv.close()

        # declare variables and lists
        state = 0
        stack = [state]
        token = ''
        accepting_state = False
        terminals_and_non_terminals = parser_table[0][1:]   # list of all terminal and non-terminals in parser table
        production_table = [['S', 3, 'E = E'],              # column 1 = production LHS, column 2 = number of RHS elements, column 3 = production RHS
                            ['S', 1, 'identifier'],
                            ['E', 3, 'E + identifier'],
                            ['E', 1, 'identifier']
                            ]

        # append the end of stack mark
        token_stream.append('$')

        # parse the token stream until all tokens are consumed and an accepting state is reached or return error if problems occur
        while accepting_state == False:
            state = stack[-1]
            token = token_stream[0]
            token_index = parser_table[0].index(token_stream[0])
            table_entry = parser_table[state + 1][token_index]
            if table_entry == '':
                print('Error: Invalid parser table entry for most recent consumed token:', token)

            # handle shifts and print updated stack, token stream, table entry and action
            if table_entry[0] == 'S':
                print('Stack =', stack, '^^^ Token Stream =', token_stream, '^^^ Table Entry =', table_entry, '^^^ Action = Shift; push', token_stream[0], '; push', table_entry[1:])
                stack.append(token)
                token_stream = token_stream[1:]
                state = int(table_entry[1:])
                stack.append(state)

                # handle shifts if accepting state is reached
                if token_stream[0] == '$' and parser_table[stack[-1] + 1][parser_table[0].index(token_stream[0])] == 'ACCT':
                    accepting_state = True
                    table_entry = parser_table[stack[-1] + 1][parser_table[0].index(token_stream[0])]
                    print('Stack =', stack, '^^^ Token Stream =', token_stream, '^^^ Table Entry =', table_entry)

            # handle reductions and print updated stack, token stream, table entry and action
            elif table_entry[0] == 'R':
                production = int(table_entry[1:])
                LHS = production_table[production - 1][0]
                RHS_count = production_table[production - 1][1]
                print('Stack =', stack, '^^^ Token Stream =', token_stream, '^^^ Table Entry =', table_entry, '^^^ Action = Reduce;', LHS, '->', production_table[production - 1][2])
                counter = 0

                # eliminate RHS of production from from stack
                while counter != RHS_count:
                    if stack[-1] in terminals_and_non_terminals:    
                        counter += 1
                    stack = stack[:-1]

                # add LHS of production and next state to stack
                if counter == RHS_count:
                    stack.append(LHS)
                    table_entry = parser_table[stack[len(stack)-2] + 1][parser_table[0].index(stack[-1])]
                    if table_entry == '':
                        print('Error: Invalid parser table entry for most recent consumed token:', token)
                    state = int(table_entry[1:])
                    stack.append(state)
                
                # handle reductions if accpeting state is reached
                if token_stream[0] == '$' and parser_table[stack[-1] + 1][parser_table[0].index(token_stream[0])] == 'ACCT':
                    accepting_state = True
                    table_entry = parser_table[stack[-1] + 1][parser_table[0].index(token_stream[0])]
                    print('Stack =', stack, '^^^ Token Stream =', token_stream, '^^^ Table Entry =', table_entry)
            
            # return error if table entry is neither shift nor reduction
            else:
                print('Error: Table entry does not indicate a Shift or a Reduction.')

        # print success/failure messgae and return status
        if table_entry == 'ACCT':
            print('\nToken stream is valid.\n')
            return 1
        else:
            print('\nInvalid toekn stream.\n')
            return 0