import JsonParser

def main():
    with open('example.json', 'r') as f:
        json = f.read()
    jp = JsonParser.JsonParser(json)
    jp.parse()

if __name__ == '__main__':
    main()
