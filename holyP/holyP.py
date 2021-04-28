from lex import *
from parse import *
from emit import *
import sys
import os
from rotateText import rotateFile, write
def main():
	print('HolyP Compiler\n')
	file = sys.argv[1]
	try:
		emitter = Emitter(sys.argv[2])
		with open(file, 'r') as inputFile:
			input = inputFile.read()
		lexer = Lexer(input)
		parser = Parser(lexer, emitter)
		parser.program()
		emitter.writeFile()
		print('Compiling Complete.')
	except:
		print('\n\nParsing Failed Trying to rotate code...\n\n')
		inFile = rotateFile(file)
		write('out.txt', inFile)
		with open('out.txt', 'r') as inputFile:
			input = inputFile.read()
		os.remove('out.txt')
		print(input)
		newEmitter = Emitter(sys.argv[2])
		newLexer = Lexer(input)
		newParser = Parser(lexer, newEmitter)
		newParser.program()
		newEmitter.writeFile()
		print('Code rotated, Compiling Complete.')
		
main()