import json as js

def handle_file():
    file = open('Easy.json')
    loaded = js.load(file)
    arrays = []

    for items in loaded['board']:
        arrays.append(items)
        for x in range(len(items)):
            if items[x] == 0:
                items[x] = ' '

    return arrays
