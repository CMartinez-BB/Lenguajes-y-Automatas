from tokentype import*
#La clase guarda el tipo del token y del texto original
class Token:
    def __init__(self, tokenText, tokenKind):
        self.text=tokenText
        self.kind=tokenKind
    @staticmethod
    def checkIfKeyword(tonkenText):
        for kind in TokenType:
            if kind.name==tonkenText and kind.value>100 and kind.value<200:
                return kind
