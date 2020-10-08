book = {}
book['tom'] = {
    'name': 'tom',
    'add': '1 red street',
    'phone': '9089898'
}
book['som'] = {
    'name': 'som',
    'add': '23 red street',
    'phone': '98998089898'
}
import json
s = json.dumps(book)
with open("C:\\data1\\book.txt", "w") as f:
    f.write(s)