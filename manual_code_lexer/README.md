Author: Brian Y. Copyright © 2022. All rights reserved.



Compile:
python lexer.py



Input (without errors):
/* comment */
int main(){
	int a = 1;
	float b = 2.0e-1;
	int c=3;
	if (c!=0){
		if(a == 1){
			c = a+b; //comment
	print("C=", c, '\n');
return 0;



Output:
PS C:\Users\PCC\Desktop\Project_1> python lexer.py
Would you like to proivde a path to the states csv file? Enter 'y' for yes, anything else to use the local diroctory file.
y
Please enter the path to the states csv file:
C:\Users\PCC\Desktop\Project_1\state.csv
Would you like to proivde a path to the tokens csv file? Enter 'y' for yes, anything else to use the local diroctory file.
y
Please enter the path to the tokens csv file:
C:\Users\PCC\Desktop\Project_1\token.csv
Would you like to proivde a path to the reserved words csv file? Enter 'y' for yes, anything else to use the local diroctory file.
y
Please enter the path to the reserved words csv file:
C:\Users\PCC\Desktop\Project_1\reserved.csv
Would you like to proivde a path to the source code text file? Enter 'y' for yes, anything else to use the local diroctory file.
y
Please enter the path to the source code text file:
C:\Users\PCC\Desktop\Project_1\code.txt
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Comment was ignored.
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  int            Lexeme:  int
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  identifier            Lexeme:  main
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  leftParen            Lexeme:  (
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  rightParen            Lexeme:  )
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  leftBrace            Lexeme:  {
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  int            Lexeme:  int
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  identifier            Lexeme:  a
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  assignOp            Lexeme:  =
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  intLiteral            Lexeme:  1
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  semicolon            Lexeme:  ;
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  float            Lexeme:  float
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  identifier            Lexeme:  b
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  assignOp            Lexeme:  =
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  floatLiteral            Lexeme:  2.0e-1
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  semicolon            Lexeme:  ;
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  int            Lexeme:  int
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  identifier            Lexeme:  c
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  assignOp            Lexeme:  =
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  intLiteral            Lexeme:  3
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  semicolon            Lexeme:  ;
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  if            Lexeme:  if
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  leftParen            Lexeme:  (
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  identifier            Lexeme:  c
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  comparator            Lexeme:  !=
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  intLiteral            Lexeme:  0
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  rightParen            Lexeme:  )
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  leftBrace            Lexeme:  {
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  if            Lexeme:  if
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  leftParen            Lexeme:  (
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  identifier            Lexeme:  a
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  comparator            Lexeme:  ==
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  intLiteral            Lexeme:  1
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  rightParen            Lexeme:  )
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  leftBrace            Lexeme:  {
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  identifier            Lexeme:  c
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  assignOp            Lexeme:  =
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  identifier            Lexeme:  a
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  addOp            Lexeme:  +
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  identifier            Lexeme:  b
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  semicolon            Lexeme:  ;
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Comment was ignored.
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  identifier            Lexeme:  print
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  leftParen            Lexeme:  (
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  string            Lexeme:  "C="
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  comma            Lexeme:  ,
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  identifier            Lexeme:  c
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  comma            Lexeme:  ,
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  char            Lexeme:  '\n'
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  rightParen            Lexeme:  )
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  semicolon            Lexeme:  ;
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  return            Lexeme:  return
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  intLiteral            Lexeme:  0
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  semicolon            Lexeme:  ;
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
End of file reached. Parsing completed.
PS C:\Users\PCC\Desktop\Project_1>



Input (with errors):
@
int main(){
	float a = 2.0e;
	print("C=", c, '\n');
return 0



Output:
PS C:\Users\PCC\Desktop\CPSC 332\Project_1> python lexer.py
Would you like to proivde a path to the states csv file? Enter 'y' for yes, anything else to use the local diroctory file.
n
Would you like to proivde a path to the tokens csv file? Enter 'y' for yes, anything else to use the local diroctory file.
n
Would you like to proivde a path to the reserved words csv file? Enter 'y' for yes, anything else to use the local diroctory file.
n
Would you like to proivde a path to the source code text file? Enter 'y' for yes, anything else to use the local diroctory file.
y
Please enter the path to the source code text file:
C:\Users\PCC\Desktop\CPSC 332\Project_1\code_with_errors.txt
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Error: Illegal character found. Check line number 1 , character number 0 (char = @ ).
Token:  int            Lexeme:  int
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  identifier            Lexeme:  main
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  leftParen            Lexeme:  (
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  rightParen            Lexeme:  )
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  leftBrace            Lexeme:  {
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  float            Lexeme:  float
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  identifier            Lexeme:  a
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  assignOp            Lexeme:  =
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Error: Unacceptable token. Check line number 3 , character number 15 (char = ; ).
Token:  identifier            Lexeme:  print
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  leftParen            Lexeme:  (
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  string            Lexeme:  "C="
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  comma            Lexeme:  ,
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  identifier            Lexeme:  c
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  comma            Lexeme:  ,
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  char            Lexeme:  '\n'
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  rightParen            Lexeme:  )
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  semicolon            Lexeme:  ;
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Token:  return            Lexeme:  return
Would like to get the next token? Enter 'y' to proceed, anything else to terminate.
y
Error: End of file reached unexpectedly. Not in an accepting state. Check line number 5 , character number 7 (char = 0 ).
PS C:\Users\PCC\Desktop\CPSC 332\Project_1>