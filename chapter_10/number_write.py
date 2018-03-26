import json

numbers = [2, 3, 4, 5, 6]

filename = 'number.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
