import JsonReader
import Stack
from Token import Token

class JsonParser:
    def __init__(self, json):
        self.jr = JsonReader.JsonReader(json)
        self.expect = Token.BEGIN
        self.stack = Stack.Stack()

    def parse(self):
        while not self.jr.isEOF():
            token = self.jr.getNextToken(self.expect)
            if token.ttype == Token.OBJECT:
                self.expect = Token.KEY
                self.stack.push(dict())
                print('OBJECT 开始 -> %s' % token.value)
            elif token.ttype == Token.KEY:
                self.expect = Token.COLON
                print('KEY -> %s' % token.value)
            elif token.ttype == Token.COLON:
                self.expect = Token.VALUE
                print('冒号 -> %s' % token.value)
            elif token.ttype == Token.STRING:
                self.expect = Token.COMMA
                print('字符串 -> %s' % token.value)
            elif token.ttype == Token.NUMBER:
                self.expect = Token.COMMA
                print('数字 -> %s' % token.value)
            elif token.ttype == Token.BOOLEAN:
                self.expect = Token.COMMA
                print('布尔 -> %s' % token.value)
            elif token.ttype == Token.NULL:
                self.expect = Token.COMMA
                print('NULL -> %s' % token.value)
            elif token.ttype == Token.COMMA:
                self.expect = Token.KEY
                print('逗号 -> %s' % token.value)
            elif token.ttype == Token.OBJECT_END:
                self.expect = Token.COMMA
                print('OBJECT 结束 -> %s' % token.value)
            elif token.ttype == Token.ARRAY:
                self.expect = Token.VALUE
                print('ARRAY 开始 -> %s' % token.value)
            elif token.ttype == Token.ARRAY_END:
                print('ARRAY 结束 -> %s' % token.value)
                self.expect = Token.COMMA
