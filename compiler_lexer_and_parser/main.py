######################################################################
# Project: Compiler grammer parser and lexical analyzer program      #
# Author: Brian Y. Copyright © 2022. All rights reserved.            #
######################################################################

# This is the main program file
# The path to the code file is hard-coded for simplicity

from lexer import Lexer
from parser import Parser

# main function
def main():
    print('\nReading and analyzing the code file using lexical analyzer...\n')
    
    # call lexer and analyze code file
    token_stream = Lexer.analize_code_chars('code.txt')

    print('\nAnalyzing completed. Token Stream =', token_stream)

    print('\nParsing the token stream...\n')

    # call parser and parse token stream produced by lexical analizer
    status = Parser.parse_token_stream(token_stream)

    # show success/failure message
    if status == 1:
        print('Program successfully analyzed and parsed the code.\n')
    else:
        print('Unknown Error: Something went wrong.\n')

    return 0

# call main function
main()