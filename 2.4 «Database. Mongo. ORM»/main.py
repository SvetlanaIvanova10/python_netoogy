# Вы реализуете приложение для поиска билетов на концерт.
# Заполните коллекцию в Монго данными о предстоящих концертах и реализуйте следующие функции:
# read_data: импорт данных из csv файла;
# find_cheapest: отсортировать билеты из базы по возрастанию цены;
# find_by_name: найти билеты по исполнителю, где имя исполнителя может быть задано не полностью, и вернуть их по возрастанию цены.

# Дополнительное задание
# Реализовать сортировку по дате мероприятия.
# Для этого вам потребуется строку с датой в csv-файле приводить к объекту datetime
# (можете считать, что все они текущего года) и сохранять его.
# Пример поиска: найти все мероприятия с 1 по 30 июля.

import csv
import re
from pprint import pprint
from datetime import datetime
from pymongo import MongoClient

client = MongoClient()
artists_db = client['concert']
artists = artists_db['artists']

def read_data(csv_file, db):

    with open(csv_file, encoding='utf8') as csvfile:
        # прочитать файл с данными и записать в коллекцию
        reader = csv.DictReader(csvfile, delimiter=',')
        artists_list = list()
        for row in reader:
            row["Цена"] = int(row["Цена"])
            row["Дата"] = datetime.strptime(f'{row["Дата"]}.2020', '%d.%m.%Y')
            artists_list.append(row)
        db.insert_many(artists_list).inserted_ids
        pprint(list(db.find()))
        return db

def find_cheapest(db):
    """
    Отсортировать билеты из базы по возрастанию цены
    Документация: https://docs.mongodb.com/manual/reference/method/cursor.sort/
    """
    sort_price = db.find().sort('Цена')
    for item in sort_price:
        print(item)




def find_by_name(name, db):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке, например "Seconds to"),
    и вернуть их по возрастанию цены
    """
    regex = re.compile(name)
    find_name = db.find({"Исполнитель": regex}).sort('Цена')
    for i in find_name:
        print(i)

def delet_all_artists(db):
    db.delete_many({})


def sort_by_date(data_with,data_by, db):
    start = datetime.strptime(f'{data_with}.2020', '%d.%m.%Y')
    end = datetime.strptime(f'{data_by}.2020', '%d.%m.%Y')
    sort_data = db.find({'Дата': {'$lt': end, '$gt': start}}).sort('Дата')
    for item in sort_data:
        print(item)

if __name__ == '__main__':
    delet_all_artists(artists)
    read_data('artists.csv', artists)
    find_cheapest(artists)
    find_by_name('L\'one', artists)
    find_by_name('Seconds to', artists)
    sort_by_date('1.01',30.03,artists)
