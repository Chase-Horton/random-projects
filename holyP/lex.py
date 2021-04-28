from tokens import *
import sys
class Lexer:
    def __init__(self, input):
        self.source = input + '\n'
        self.curChar = ''
        self.index = -1
        self.nextChar()

    def nextChar(self):
        self.index +=1
        if self.index >= len(self.source):
            self.curChar = '\0'  # EOF
        else:
            self.curChar = self.source[self.index]

    def peek(self):
        if (self.index + 1>= len(self.source)):
            return '\0' # EOF
        return self.source[self.index+ 1]

    #Call for errors
    def errorAbort(self, message):
        #change to a holy print
        print('\nProgram Halted Early!')
        print('Lexing error\n' + '----------------------\n' + message)
        sys.exit(0)

    def skipSpaces(self):
        while self.curChar == ' ' or self.curChar == '\t' or self.curChar =='\r':
            self.nextChar()
    
    def skipComments(self):
        if self.curChar == '~':
            while self.curChar != '\n':
                self.nextChar()

    def getToken(self):
        token = None
        self.skipSpaces()
        self.skipComments()
        if(self.curChar == '+'):
            token = Token(self.curChar, TokenType.PLUS)

        elif(self.curChar == '-'):
            token = Token(self.curChar, TokenType.MINUS)

        elif(self.curChar == '/'):
            token = Token(self.curChar, TokenType.SLASH)

        elif(self.curChar == '*'):
            token = Token(self.curChar, TokenType.ASTERISK)

        elif(self.curChar == '\n'):
            token = Token(self.curChar, TokenType.NEWLINE)

        elif(self.curChar == '\0'):
           token = Token(self.curChar, TokenType.EOF)

        elif(self.curChar == '='):
            if(self.peek() == '='):
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar+self.curChar, TokenType.EQEQ)

            else:
                token = Token(self.curChar, TokenType.EQ)
    
        elif self.curChar == '>':
            # Check whether this is token is > or >=

            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.GTEQ)

            else:
                token = Token(self.curChar, TokenType.GT)

        elif self.curChar == '<':
                # Check whether this is token is < or <=
                if self.peek() == '=':
                    lastChar = self.curChar
                    self.nextChar()
                    token = Token(lastChar + self.curChar, TokenType.LTEQ)

                else:
                    token = Token(self.curChar, TokenType.LT)

        elif self.curChar == '!':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.NOTEQ)

            else:
                self.abort("Expected !=, got !" + self.peek())
        
        elif self.curChar == '\"':
            self.nextChar()
            startPos = self.index
            while self.curChar != '\"':
                if self.curChar == '\r' or self.curChar == '\n' or self.curChar == '\t' or self.curChar == '\\' or self.curChar == '%':
                    self.abort("Illegal character in string.")
                self.nextChar()
            
            txt = self.source[startPos:self.index]
            token = Token(txt, TokenType.STRING)

        elif self.curChar.isdigit():
            startPos = self.index
            while self.peek().isdigit():
                self.nextChar()
            if(self.peek() == '.'):
                self.nextChar()

                if(not self.peek().isdigit()):
                    self.errorAbort('Unresolved Decimal Point after Number.')
                
                while self.peek().isdigit():
                    self.nextChar()
                
            text = self.source[startPos : self.index + 1]
            token = Token(text, TokenType.NUMBER)
        
        elif self.curChar.isalpha():
        #char is a letter so it is either a keyword or identifier
            startPos = self.index
            while self.peek().isalnum():
                self.nextChar()
            text = self.source[startPos : self.index + 1]
            keyword = Token.checkIfKeyword(text)
            if keyword == None:
                token = Token(text, TokenType.IDENT)
            else:
                token = Token(text, keyword)
        else:
            # Unknown Token
            self.errorAbort('Unknown Token: ' + self.curChar)

        self.nextChar()
        return token