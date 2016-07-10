
class Token:
    BEGIN = 'BEGIN'
    OBJECT = 'OBJECT'
    ARRAY = 'ARRAY'
    KEY = 'KEY'
    COLON = 'COLON'
    VALUE = 'VALUE'
    COMMA = 'COMMA'
    OBJECT_END = 'OBJECT_END'
    ARRAY_END = 'ARRAY_END'
    def __init__(self, ttype, value):
        self.ttype = ttype
        self.value = value

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '<Token %s: %s>' % ( self.ttype, self.value)
