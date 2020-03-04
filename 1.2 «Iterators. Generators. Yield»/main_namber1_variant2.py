import json
from pprint import pprint


def check_site(path):
    name_link = []
    with open(path, encoding='utf8') as name_file:
        for url in name_file:
            url = url.strip().replace(' ', '_')
            name_link.append(f'{url} - https://en.wikipedia.org/wiki/{url}')
            yield name_link
    with open('countries_link1.json', 'w', encoding='utf-8') as name_countries:
        name_countries.write(json.dumps(name_link))

if __name__ == '__main__':
    for link in check_site('name_countries.list'):
        pass
    with open("countries_link1.json", encoding="utf-8") as datafile:
        json_data = json.load(datafile)
        pprint(json_data, indent=2, depth=5, width=150)