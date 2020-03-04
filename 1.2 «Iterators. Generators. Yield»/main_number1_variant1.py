import json
from pprint import pprint


name_link = []
class CheckSite:

    def __init__(self, path):
        self.file = open(path, encoding='utf8')
        # self.session = requests.Session()

    def __iter__(self):
        return self

    def __next__(self):
        host = self.file.readline().strip().replace(' ', '_')
        if not host:
            raise StopIteration
        name_link.append(f'{host} - https://en.wikipedia.org/wiki/{host}')
        with open('countries_link.json', 'w', encoding='utf-8') as name_countries:
            name_countries.write(json.dumps(name_link))


if __name__ == '__main__':
    for link in CheckSite('name_countries.list'):
        pass
    with open("countries_link.json", encoding="utf-8") as datafile:
        json_data = json.load(datafile)
        pprint(json_data, indent=2, depth=5, width=150)


