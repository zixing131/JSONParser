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
            print(self.stack.stack)
            token = self.jr.getNextToken(self.expect)
            if token.ttype == Token.OBJECT:
                self.stack.push(dict())
                self.expect = Token.KEY
                print('OBJECT 开始 -> %s' % token.value)
            elif token.ttype == Token.KEY:
                self.stack.push(token)
                self.expect = Token.COLON
                print('KEY -> %s' % token.value)
            elif token.ttype == Token.COLON:
                self.expect = Token.VALUE
                print('冒号 -> %s' % token.value)
            elif token.ttype == Token.VALUE:
                if self.stack.getLatestType() == dict:
                    key = self.stack.get().value
                    self.stack.stack[-1][key] = token.value
                elif self.stack.getLatestType() == list:
                    self.stack.stack[-1].append(token.value)
                self.expect = Token.COMMA
                print('Value -> %s' % token.value)
            elif token.ttype == Token.COMMA:
                if self.stack.getLatestType() == dict:
                    self.expect = Token.KEY
                elif self.stack.getLatestType() == list:
                    self.expect = Token.VALUE
                print('逗号 -> %s' % token.value)
            elif token.ttype == Token.OBJECT_END:
                if len(self.stack.stack) == 1:
                    return self.stack.get()
                if self.stack.getParentType() == dict:
                    value = self.stack.get()
                    key = self.stack.get().value
                    self.stack.stack[-1][key] = value
                elif self.stack.getParentType() == list:
                    value = self.stack.get()
                    self.stack.stack[-1].append(value)
                self.expect = Token.COMMA
                print('OBJECT 结束 -> %s' % token.value)
            elif token.ttype == Token.ARRAY:
                self.stack.push(list())
                self.expect = Token.VALUE
                print('ARRAY 开始 -> %s' % token.value)
            elif token.ttype == Token.ARRAY_END:
                if len(self.stack.stack) == 1:
                    return self.stack.get()
                value = self.stack.get()
                key = self.stack.get().value
                self.stack.stack[-1][key] = value
                self.expect = Token.COMMA
                print('ARRAY 结束 -> %s' % token.value)
            
