documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006"}
]

def people(document):
    try:
        for doc in document:
            if doc['name'] != " ":
                print(doc["name"])
    except KeyError:
        print("Имя отсутствует")

if __name__ == '__main__':
    people(documents)
