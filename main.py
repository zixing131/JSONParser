import JsonParser

def main():
    with open('example.json', 'r') as f:
        json = f.read()
    jp = JsonParser.JsonParser(json)
    print(jp.parse())

if __name__ == '__main__':
    main()
