
class Token:
    BEGIN = 'BEGIN'
    OBJECT = 'OBJECT'
    ARRAY = 'ARRAY'
    KEY = 'KEY'
    COLON = 'COLON'
    VALUE = 'VALUE'
    STRING = 'STRING'
    COMMA = 'COMMA'
    NUMBER = 'NUMBER'
    BOOLEAN = 'BOOLEAN'
    NULL = 'NULL'
    OBJECT_END = 'OBJECT_END'
    ARRAY_END = 'ARRAY_END'
    def __init__(self, ttype, value):
        self.ttype = ttype
        self.value = value

    def __str__(self):
        return '<Token %s: %s>' % ( self.ttype, self.value)
