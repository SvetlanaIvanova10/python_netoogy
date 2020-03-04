import json


def countries(name_file):
    with open(name_file, encoding="utf-8") as datafile:
        json_data = json.load(datafile)
    list_name = []
    for iter in json_data:
        name = iter['name']['common']
        list_name.append(name)
    with open('name_countries.list', 'w', encoding='utf-8') as name_countries:
        for element in list_name:
            name_countries.write(f'{element} \n')


if __name__ == '__main__':
    countries("countries.json")
