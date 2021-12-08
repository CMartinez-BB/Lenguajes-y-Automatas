from _typeshed import Self
import sys
from token import Token 
from tokentype import *

class Lexer:
    #Constructor
    def __init__(self, input) :
        self.source= input
        self.curChar= ' ' 
        self.curPos= -1
        self.nextChar()
    #Procesa el caracter actual
    def nextChar(self):
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar= '\0' #EOF End Of File 
        else:
            self.curChar = self.source[self.curPos]
    #anticipa el caracter que sigue 
    def peek(self):
        if self.curPos + 1>= len(self.source):
            return '\0'
        return self.source[self.curPos + 1]

    #Muestra el error por si hay un token invalido
    def abortar(self, message):
        sys.exit("Error de lexico"+message)
    #Saltearse los espacios en blancos 
    def skipWhiteSpace(self):
        while self.curChar==' ' or self.curChar=='\t' or self.curChar=='\r':
            self.curChar()
    #Skip comentarios
    def skipComment(self):
        if self.curChar=='#':
            while self.curChar !="\n":
                self.nextChar()
    #determina los tipos de tokens 
    def getToken(self):
        self.skipWhiteSpace()
        self.skipComment()
        #checar primero si el primer caracter es diferente a una operación  
        if self.curChar=='+':
            token=Token(self.curChar,TokenType.PLUS)
        elif self.curChar=='-':
            token=Token(self.curChar,TokenType.MINUS)
        elif self.curChar=='*':
            token=Token(self.curChar,TokenType.ASTERISK)
        elif self.curChar=='/':
            token=Token(self.curChar,TokenType.SLASH)
        elif self.curChar=='=':
            #verificar si estan asignando o comparando
            if self.peek()=='=':
                lastChar=self.curChar
                self.nextChar()
                token=Token(lastChar+self.curChar,TokenType.EQEQ)
            else:
                token=Token(self.curChar,TokenType.EQ)
        elif self.curChar=='>':
            #Verificar si hay un mayor que 
            if self.peek()=='=':
                lastChar=self.curChar
                self.nextChar()
                token=Token(lastChar+self.curChar,TokenType.GTEQ)
            else:
                token=Token(self.curChar,TokenType.GT)
        elif self.curChar=='<':
            if self.peek()=='=':
                lastChar=self.curChar
                self.nextChar()
                token=Token(lastChar+self.curChar,TokenType.LTEQ)
            else:
                token=Token(Self.curChar, TokenType.LT)
        elif self.curChar=='!':
            if self.peek()=='=':
                lastChar=self.curChar
                self.nextChar()
                token=Token(lastChar+self.curChar,TokenType.NOTEQ)
            else:
                self.abort("Se esperaba un != y escribiste un !"+self.peek())
        elif self.curChar=='\"':
            self.nextChar()
            startPos=self.curPos
            while self.curChar!='\"':
                if self.curChar=='\r' or self.curChar=='\n' or self.curChar=='\t' or self.curChar=='\\' or self.curChar=='%':
                    self.abort("Caracter no validoo en el string")
                self.nextChar()

            tokenText=self.source[startPos: self.curPos]
            token=Token(tokenText, TokenType.STRING)
        #Capturar numeros
        elif self.curChar.isdigit():
            startPos=self.curPos
            while self.peek().isdigit():
                self.curChar()
            if self.peek()=='':
                self.nextChar()
                if not self.peek().isdigit():
                    self.abort("Caracter no valido en el número")
                while self.peek().isdigit():
                    self.nextChar()
            tokenText=self.source[startPos: self.curPos+1]
            tokenText=Token(tokenText, TokenType.STRING)
        elif self.curChar.isalpha():
            startPos=self.curPos
            while self.peek().isalnum():
                self.nextChar()
            tokenText=self.source[startPos: self.curPos+1]
            keyboard=Token.checkIfKeyword(tokenText)
            if keyboard==None:
                token=Token(tokenText, TokenType.IDENT)
            else:
                token=Token(tokenText, keyboard)


