from lex import *
import sys
		
def main():
	print('HolyP Lexer\n')

	if len(sys.argv) != 2:
		# sys.exit('Please supply source file as argument.')
		file = 'test.holyP'
	else:
		file = sys.argv[1]

	with open(file, 'r') as inputFile:
		input = inputFile.read()

	lexer = Lexer(input)
	token = lexer.getToken()
	while token.kind != TokenType.EOF:
		print(token.kind)
		token = lexer.getToken()

	print('Lexing Complete.')

main()