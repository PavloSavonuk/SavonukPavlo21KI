dictionary = {
    'name': 'Savonuk',
    'age': 16,
    'dict': {'1': 'toplik',
             '2': 'Hello world',
             '3': 2545,
             '4': False,
             '5': True},
    'python': 'pitun',
}
print(dictionary)

type_dict = {}
for key, value in dictionary.items():
    if type(value) == dict:
        for key1, value1 in value.items():
            type_dict[key1] = type(value1)
    else:
        type_dict[key] = type(value)
print(type_dict)
