import enum
class Token:
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText
        self.kind = tokenKind

    @staticmethod
    def checkIfKeyword(tokenText):
        for kind in TokenType:
            # Relies on all keyword enum values being 1XX.
            if kind.name == tokenText and kind.value >= 100 and kind.value < 200:
                return kind
        return None

class TokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3
    #Keywords
    MARK = 101
    GOTO = 102
    PREACH = 103
    CONFESS = 104
    LET = 105
    IF = 106
    GOD = 107
    PERMITS = 108
    THEN = 109
    ENDIF = 110
    WHILE = 111
    REPEAT = 112
    ENDWHILE = 113
    PRAY = 124
    # Operators.
    EQ = 201  
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211