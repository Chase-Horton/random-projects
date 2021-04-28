from lex import *
import sys
from tokens import *

# tracks current token and checks if the code matches grammar
class Parser:
	def __init__(self, lexer):
		self.lexer = lexer

		self.symbols = set()
		self.marksDeclared = set()
		self.marksGoToed = set()

		self.curToken = None
		self.peekToken = None
		self.nextToken()
		self.nextToken()

	def checkToken(self, kind):
		return kind == self.curToken.kind

	def checkPeek(self, kind):
		return kind == self.peekToken.kind

	def match(self, kind):
		if not self.checkToken(kind):
			self.abort("Expected " + kind.name + ", got " + self.curToken.kind.name)
		self.nextToken()

	def nextToken(self):
		self.curToken = self.peekToken
		self.peekToken = self.lexer.getToken()

	def abort(self, message):
		print('\nProgram Halted Early!')
		print('Parsing error\n' + '----------------------\n' + message)
		sys.exit(0)


	# Rules

	# program ::= {statement}
	def program(self):
		print('PROGRAM')

		# ignore newlines at start
		while self.checkToken(TokenType.NEWLINE):
			self.nextToken()

		#parse all statements in program
		while not self.checkToken(TokenType.EOF):
			self.statement()
		
		for mark in self.marksGoToed:
			if mark not in self.marksDeclared:
				self.abort('Attempting to GOTO an undefined mark: ' + mark)


	# statements in program
	def statement(self):
		print(self.curToken.text)
		# (print) PREACH (expression | string) nl
		if self.checkToken(TokenType.PREACH):
			print('STATEMENT-PRINT')
			self.nextToken()

			if(self.checkToken(TokenType.STRING)):
				# simple string
				self.nextToken()
			else:
				# contains expression
				self.expression()

		# "IF" "GOD" "PERMITS" comparison "THEN" nl {statement} "ENDIF" nl
		elif self.checkToken(TokenType.IF):
			self.nextToken()
			self.match(TokenType.GOD)
			self.match(TokenType.PERMITS)
			print('STATEMENT-IF')

			self.comparison()

			self.match(TokenType.THEN)
			self.nl()

			while not self.checkToken(TokenType.ENDIF):
				self.statement()

			self.match(TokenType.ENDIF)

		# "WHILE" comparison "REPEAT" nl {statement} "ENDWHILE" nl
		elif self.checkToken(TokenType.WHILE):
			print("STATEMENT-WHILE")
			self.nextToken()
			self.comparison()

			self.match(TokenType.REPEAT)
			self.nl()

			# Zero or more statements in the loop body.
			while not self.checkToken(TokenType.ENDWHILE):
				self.statement()

			self.match(TokenType.ENDWHILE)

 		# "MARK" ident
		elif self.checkToken(TokenType.MARK):
			print("STATEMENT-MARK")
			self.nextToken()
			if self.curToken.text in self.marksDeclared:
				self.abort('Mark already exists: ' + self.curToken.text)
			self.marksDeclared.add(self.curToken.text)

			self.match(TokenType.IDENT)

		# "GOTO" ident
		elif self.checkToken(TokenType.GOTO):
			print("STATEMENT-GOTO")
			self.nextToken()
			self.marksGoToed.add(self.curToken.text)
			self.match(TokenType.IDENT)

		# "LET" ident "=" expression
		elif self.checkToken(TokenType.PRAY):
			self.nextToken()
			print("STATEMENT-LET")

			if self.curToken.text not in self.symbols:
				self.symbols.add(self.curToken.text)
			self.match(TokenType.IDENT)
			self.match(TokenType.EQ)
			self.expression()

		# "INPUT" ident
		elif self.checkToken(TokenType.CONFESS):
			print("STATEMENT-INPUT")
			self.nextToken()
			if self.curToken.text not in self.symbols:
				self.symbols.add(self.curToken.text)
			self.match(TokenType.IDENT)

		# This is not a valid statement. Error!
		else:
			self.abort("Invalid statement at " + self.curToken.text + " (" + self.curToken.kind.name + ")")
		# newline
		self.nl()

	# nl ::= '\n'+
	def nl(self):
		print("NEWLINE")
		self.match(TokenType.NEWLINE)

		while self.checkToken(TokenType.NEWLINE):
			self.nextToken()

	def isComparisonOperator(self):
		return self.checkToken(TokenType.GT) or self.checkToken(TokenType.GTEQ) or self.checkToken(TokenType.LT) or self.checkToken(TokenType.LTEQ) or self.checkToken(TokenType.EQEQ) or self.checkToken(TokenType.NOTEQ)
	
	# comparison ::= expression (("==" | "!=" | ">" | ">=" | "<" | "<=") expression)+
	def comparison(self):
		print('COMPARISON')

		self.expression()

		# need at least one comparison operator
		if self.isComparisonOperator():
			self.nextToken()
			self.expression()
		# no comparison operator found
		else:
			self.abort("Expected comparison operator at " + self.curToken.text)
		
		#check for more comparisons
		while self.isComparisonOperator():
			self.nextToken()
			self.expression()
	# expression ::= term {( "-" | "+" ) term}
	def expression(self):
		print("EXPRESSION")

		self.term()

		while self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
			self.nextToken()
			self.term()
	
	# term ::= unary {( "/" | "*" ) unary}
	def term(self):
		print("TERM")

		self.unary()

		while self.checkToken(TokenType.SLASH) or self.checkToken(TokenType.ASTERISK):
			self.nextToken()
			self.unary()
	# unary ::= ["+" | "-"] primary
	def unary(self):
		print("UNARY")

		self.primary()

		while self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
			self.nextToken()
			self.primary()
	# primary ::= number | ident
	def primary(self):
		print("PRIMARY (" + self.curToken.text + ")")

		if self.checkToken(TokenType.NUMBER):
			self.nextToken()
		elif self.checkToken(TokenType.IDENT):
			# check that variable exists
			if self.curToken.text not in self.symbols:
				self.abort('Refrencing Variable before assignment: ' + self.curToken.text)
			self.nextToken()
		else:
			# error
			self.abort("Unexpected token at " + self.curToken.text)