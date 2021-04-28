from lex import *
from parse import *
from emit import *
import sys
import os
from rotateText import rotateFile, write

def main():
	print('HolyP Compiler\n')
	file = sys.argv[1]
	emitter = Emitter(sys.argv[2])
	try:
		with open(file, 'r') as inputFile:
			input = inputFile.read()
		lexer = Lexer(input)
		parser = Parser(lexer, emitter)
		parser.program()
		emitter.writeFile()
		print('Compiling Complete.')
	except:
		print('\n\nParsing Failed Trying to rotate code...')
		inFile = rotateFile(file)
		write('out.txt', inFile)
		with open('out.txt', 'r') as inputFile:
			input = inputFile.read()
		os.remove('out.txt')
		lexer = Lexer(input)
		parser = Parser(lexer, emitter)
		parser.program()
		emitter.writeFile()
		print('Code rotated, Compiling Complete.')
		
main()