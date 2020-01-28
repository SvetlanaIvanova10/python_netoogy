from pprint import pprint
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

def out_cook_book(cook_book):
    print('cook_book =')
    pprint(cook_book, indent=3, depth=3, width=150)

def get_shop_list_by_dishes(dishes, person_count):
    cook_book_ingridients = dict_recipes()
    ingridients = {}
    for dis in dishes:
        if dis in cook_book_ingridients.keys():
            for ing in cook_book_ingridients[dis]:
                keys = ing.get('ingredient_name')
                count = {'measure': ing.get('measure'), 'quantity': int(ing.get('quantity'))*person_count}
                if keys not in ingridients.keys():
                    ingridients[keys] = count
                else:
                    new_count = {'measure': count.get('measure'), 'quantity': int(count.get('quantity')) * person_count}
                    ingridients[keys] = new_count
        else:
            print('нет такого рецепта')
    pprint(ingridients)

if __name__ == '__main__':
    # Я сделала в разных with, потому что,если запустить в одном, то выполняется правильно только первая функция
    #

    with open("recipes.txt", encoding='utf8') as recipes:
        out_cook_book(dict_recipes())
        recipes.seek(0)
        get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)
