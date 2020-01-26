def dict_recipes():
    cook_book = {}
    for line in recipes:
        if '|' not in line and line != '\n' and not line[0].isdigit():
            key = line.rstrip()
        elif '|' in line and not line[0].isdigit():
            if line == '\n':
                continue
            else:
                value = line.rstrip()
                split_ratings = value.split('|')
                ratings = {'ingredient_name': split_ratings[0], 'quantity': split_ratings[1],
                           'measure': split_ratings[2]}
                if key not in cook_book.keys():
                    cook_book[key] = list()
                cook_book[key].append(ratings)
    return cook_book


def out_cook_book(cook_book_):
    print('cook_book = {')
    for number in cook_book_.keys():
        print(' "{}": [\n   {}\n   ],'.format(number, '\n   '.join(map(str, cook_book_[number]))))
    print('}')

def get_shop_list_by_dishes(dishes, person_count):
    cook_book_ingridients = dict_recipes()
    ingridients = {}
    for dis in dishes:
        if dis  in cook_book_ingridients.keys():
            for ing in cook_book_ingridients[dis]:
                keys = ing.get('ingredient_name')
                count = {'measure': ing.get('measure'), 'quantity': int(ing.get('quantity'))*person_count}
                if keys not in ingridients.keys():
                    ingridients[keys] = list()
                ingridients[keys].append(count)
        else:
            print('нет такого рецепта')
    print("{")
    for number in ingridients.keys():
        print(' "{}": {},'.format(number, '\n   '.join(map(str, ingridients[number]))))
    print("}")

if __name__ == '__main__':
    with open("recipes.txt", encoding='utf8') as recipes:
        out_cook_book(dict_recipes())
    print()
    with open("recipes.txt", encoding='utf8') as recipes:
        get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
