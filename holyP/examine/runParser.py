from lex import *
from parse import *
import sys
def main():
	print('HolyP Compiler\n')


	if len(sys.argv) != 2:
		# sys.exit('Please supply source file as argument.')
		file = 'test.holyP'
	else:
		file = sys.argv[1]


	with open(file, 'r') as inputFile:
		input = inputFile.read()

	lexer = Lexer(input)
	parser = Parser(lexer)

	parser.program()

	print('Parsing Complete.')

main()