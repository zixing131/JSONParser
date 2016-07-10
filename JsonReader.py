import JsonParser
from Token import Token

class JsonReader:
    def __init__(self, json):
        self.point = 0
        self.json = json
        self.length = len(self.json)

    def isValidChar(self, char):
        invalidChars = (' ', '\n')
        for c in invalidChars:
            if c == char:
                return False
        return True

    def getChar(self):
        c = self.json[self.point]
        self.point += 1
        return c

    def peekChar(self):
        return self.json[self.point]

    def getNextChar(self):
        flag = True
        while flag:
            char = self.json[self.point]
            if self.isValidChar(char):
                flag = False
            self.point += 1
        return char

    def peekNextChar(self):
        flag = True
        while flag:
            char = self.json[self.point]
            if self.isValidChar(char):
                break
            else:
                self.point += 1
        return char

    def isEOF(self):
        if self.length <= self.point + 1:
            return True
        return False

    def getNextToken(self, expect):
        print(expect)
        char = self.getNextChar()
        if expect == Token.BEGIN:
            if char == '{':
                return Token(Token.OBJECT, char)
            elif char == '[':
                return Token(Token.ARRAY, char)
            else:
                raise Exception('Invalid Char: %s' % char)
        elif expect == Token.KEY:
            if char == '"':
                return Token(Token.KEY, self.getString())
            if char == '{':
                return Token(Token.OBJECT, char)
            if char == '}':
                return Token(Token.OBJECT_END, char)
            else:
                raise Exception('Invalid Char: %s' % char)
        elif expect == Token.COLON:
            if char == ':':
                return Token(Token.COLON, char)
            else:
                raise Exception('Invalid Char: %s' % char)
        elif expect == Token.VALUE:
            if char == '"':
                return Token(Token.VALUE, self.getString())
            elif char.isdigit() or char == '-' or char == '+':
                return Token(Token.VALUE, self.getNumber(char))
            elif char == 'f' or char == 't':
                return Token(Token.VALUE, self.getBoolean(char))
            elif char == 'n':
                return Token(Token.VALUE, self.getNull(char))
            elif char == '{':
                return Token(Token.OBJECT, char)
            elif char == '[':
                return Token(Token.ARRAY, char)
            else:
                raise Exception('Invalid Char: %s' % char)
        elif expect == Token.COMMA:
            if char == ',':
                return Token(Token.COMMA, char)
            elif char == '}':
                return Token(Token.OBJECT_END, char)
            elif char == ']':
                return Token(Token.ARRAY_END, char)
            else:
                raise Exception('Invalid Char: %s' % char)
        elif expect == Token.OBJECT:
            if char == '"':
                return Token(Token.KEY, char)
            elif char == '}':
                return Token(Token.OBJECT_END, char)
        elif expect == Token.ARRAY:
            if char == ']':
                return Token(Token.ARRAY_END, char)
            return Token(Token.VALUE, char)

    def getNull(self, char):
        res = char
        while True:
            c = self.peekChar()
            if c == ',' or c == '}' or c == ']':
                break
            c = self.getChar()
            res += c
        if res == 'null':
            n = None
        else:
            raise Exception('Invalid Value: %s' % res)
        return n


    def getBoolean(self, char):
        res = char
        while True:
            c = self.peekChar()
            if c == ',' or c == '}' or c == ']':
                break
            c = self.getChar()
            res += c
        if res == 'false':
            b = False
        elif res == 'true':
            b = True
        else:
            raise Exception('Invalid Value: %s' % res)
        return b


    def getNumber(self, char):
        res = char
        while True:
            c = self.peekChar()
            if c == ',' or c == '}' or c == ']':
                break
            c = self.getChar()
            res += c
             
        isPoint = False
        for i in res:
            if i == '.' or i == 'e' or i == 'E':
                isPoint = True
                break
             
        if isPoint:
                result = float(res)
        else:
                result = int(res)
        return result


    def getString(self):
        res = ''
        while True:
            c = self.getChar()
            if c == '"':
                return res
            res += c
