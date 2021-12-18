# definir todos los tokens enumerarlos
import enum
class TokenType(enum.Enum):
    EOF = -1
    NEWLINE  = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3
    ##KEYWORDS
    
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 10
    REEAT = 110
    ENDWHILE = 111
    DECLARA = 112
    COMO = 113
    GG = 114
    BLINKEAR = 115
    BUFEAR = 116
    F = 117
    LOOTEAR = 118
    BORRAR=119
    INSERTAR=120
    
    #OPERADORES 
    EQ= 201
    PLUS =202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT =  208
    LTEQ= 209
    GT = 210
    GTEQ = 211
