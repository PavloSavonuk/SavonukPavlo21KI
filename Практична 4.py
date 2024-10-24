dictionary = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "Baker Street",
        "city": "London",
        "postal_code": "NW1",
        "country": "UK",
        "building": "221B"
    },
    "married": True
}

types_dictionary = {
    "name": str,
    "age": int,
    "address": {
        "street": str,
        "city": str,
        "postal_code": str,
        "country": str,
        "building": str
    },
    "married": bool
}

print(dictionary)
print(types_dictionary)