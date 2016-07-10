class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def get(self):
        return self.stack.pop()

    def getLatestType(self):
        i = -1
        while True:
            if type(self.stack[i]) == dict:
                return dict
            elif type(self.stack[i]) == list:
                return list
            i -= 1

    def getParentType(self):
        i = -2
        while True:
            if type(self.stack[i]) == dict:
                return dict
            elif type(self.stack[i]) == list:
                return list
            i -= 1

