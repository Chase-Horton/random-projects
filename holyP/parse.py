from lex import *
import sys
from tokens import *

# tracks current token and checks if the code matches grammar
class Parser:
	def __init__(self, lexer, emitter):
		self.lexer = lexer
		self.emitter = emitter

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
		self.emitter.headerLine('#include <stdio.h>')
		self.emitter.headerLine('int main(void){')

		# ignore newlines at start
		while self.checkToken(TokenType.NEWLINE):
			self.nextToken()

		#parse all statements in program
		while not self.checkToken(TokenType.EOF):
			self.statement()
		
		self.emitter.emitLine('return 0;')
		self.emitter.emitLine('}')

		for mark in self.marksGoToed:
			if mark not in self.marksDeclared:
				self.abort('Attempting to GOTO an undefined mark: ' + mark)


	# statements in program
	def statement(self):

		# (print) PREACH (expression | string) nl
		if self.checkToken(TokenType.PREACH):
			self.nextToken()

			if(self.checkToken(TokenType.STRING)):
				# simple string
				self.emitter.emitLine("printf(\"" + self.curToken.text + '\\n\");')
				self.nextToken()
			else:
				# contains expression
				self.emitter.emit("printf(\"%" + ".2f\\n\", (float)(")
				self.expression()
				self.emitter.emitLine('));')

		# "IF" "GOD" "PERMITS" comparison "THEN" nl {statement} "ENDIF" nl
		elif self.checkToken(TokenType.IF):
			self.nextToken()
			self.match(TokenType.GOD)
			self.match(TokenType.PERMITS)

			self.emitter.emit('if(')
			self.comparison()

			self.match(TokenType.THEN)
			self.nl()
			self.emitter.emitLine('){')

			while not self.checkToken(TokenType.ENDIF):
				self.statement()

			self.match(TokenType.ENDIF)
			self.emitter.emitLine('}')
		# "WHILE" comparison "REPEAT" nl {statement} "ENDWHILE" nl
		elif self.checkToken(TokenType.WHILE):
			self.nextToken()

			self.emitter.emit('while(')
			self.comparison()

			self.match(TokenType.REPEAT)
			self.nl()
			self.emitter.emitLine('){')

			# Zero or more statements in the loop body.
			while not self.checkToken(TokenType.ENDWHILE):
				self.statement()

			self.match(TokenType.ENDWHILE)
			self.emitter.emitLine('}')
 		# "MARK" ident
		elif self.checkToken(TokenType.MARK):
#			print("STATEMENT-MARK")
			self.nextToken()
			if self.curToken.text in self.marksDeclared:
				self.abort('Mark already exists: ' + self.curToken.text)
			self.marksDeclared.add(self.curToken.text)

			self.emitter.emitLine(self.curToken.text + ":")
			self.match(TokenType.IDENT)

		# "GOTO" ident
		elif self.checkToken(TokenType.GOTO):
#			print("STATEMENT-GOTO")
			self.nextToken()
			self.marksGoToed.add(self.curToken.text)
			self.emitter.emitLine('goto ' + self.curToken.text + ';')
			self.match(TokenType.IDENT)

		# "LET" ident "=" expression
		elif self.checkToken(TokenType.PRAY):
#			print("STATEMENT-LET")
			self.nextToken()

			if self.curToken.text not in self.symbols:
				self.symbols.add(self.curToken.text)
				self.emitter.headerLine("float " + self.curToken.text + ';')
			self.emitter.emit(self.curToken.text + '=')
			self.match(TokenType.IDENT)
			self.match(TokenType.EQ)

			self.expression()
			self.emitter.emitLine(';')
		# "INPUT" ident
		elif self.checkToken(TokenType.CONFESS):
#			print("STATEMENT-INPUT")
			self.nextToken()
 			# If variable doesn't already exist, declare it.
			if self.curToken.text not in self.symbols:
				self.symbols.add(self.curToken.text)
				self.emitter.headerLine("float " + self.curToken.text + ";")

			# Emit scanf but also validate the input. If invalid, set the variable to 0 and clear the input.
			self.emitter.emitLine("if(0 == scanf(\"%" + "f\", &" + self.curToken.text + ")) {")
			self.emitter.emitLine(self.curToken.text + " = 0;")
			self.emitter.emit("scanf(\"%")
			self.emitter.emitLine("*s\");")
			self.emitter.emitLine("}")
			self.match(TokenType.IDENT)

		# This is not a valid statement. Error!
		else:
			self.abort("Invalid statement at " + self.curToken.text + " (" + self.curToken.kind.name + ")")
		# newline
		self.nl()

	# nl ::= '\n'+
	def nl(self):
#		print("NEWLINE")
		self.match(TokenType.NEWLINE)

		while self.checkToken(TokenType.NEWLINE):
			self.nextToken()

	def isComparisonOperator(self):
		return self.checkToken(TokenType.GT) or self.checkToken(TokenType.GTEQ) or self.checkToken(TokenType.LT) or self.checkToken(TokenType.LTEQ) or self.checkToken(TokenType.EQEQ) or self.checkToken(TokenType.NOTEQ)
	
	# comparison ::= expression (("==" | "!=" | ">" | ">=" | "<" | "<=") expression)+
	def comparison(self):
#		print('COMPARISON')

		self.expression()

		# need at least one comparison operator
		if self.isComparisonOperator():
			self.emitter.emit(self.curToken.text)
			self.nextToken()
			self.expression()
		# no comparison operator found
		else:
			self.abort("Expected comparison operator at " + self.curToken.text)
		
		#check for more comparisons
		while self.isComparisonOperator():
			self.emitter.emit(self.curToken.text)
			self.nextToken()
			self.expression()
	# expression ::= term {( "-" | "+" ) term}
	def expression(self):
#		print("EXPRESSION")

		self.term()

		while self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
			self.emitter.emit(self.curToken.text)
			self.nextToken()
			self.term()
	
	# term ::= unary {( "/" | "*" ) unary}
	def term(self):
#		print("TERM")

		self.unary()

		while self.checkToken(TokenType.SLASH) or self.checkToken(TokenType.ASTERISK):
			self.emitter.emit(self.curToken.text)
			self.nextToken()
			self.unary()
	# unary ::= ["+" | "-"] primary
	def unary(self):
#		print("UNARY")

		self.primary()

		while self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
			self.emitter.emit(self.curToken.text)
			self.nextToken()
			self.primary()
	# primary ::= number | ident
	def primary(self):
#		print("PRIMARY (" + self.curToken.text + ")")

		if self.checkToken(TokenType.NUMBER):
			self.emitter.emit(self.curToken.text)
			self.nextToken()
		elif self.checkToken(TokenType.IDENT):
			# check that variable exists
			if self.curToken.text not in self.symbols:
				self.abort('Refrencing Variable before assignment: ' + self.curToken.text)
			self.emitter.emit(self.curToken.text)
			self.nextToken()
		else:
			# error
			self.abort("Unexpected token at " + self.curToken.text)