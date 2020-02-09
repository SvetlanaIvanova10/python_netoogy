# Вывести список групп в ВК в которых состоит пользователь, но не состоит никто из его друзей.
# В качестве жертвы, на ком тестировать, можно использовать: https://vk.com/eshmargunov
#
# Входные данные:
# Имя пользователя или его id в ВК, для которого мы проводим исследование.
# Внимание: и имя пользователя (eshmargunov) и id (171691064) - являются валидными входными данными.
# Ввод можно организовать любым способом:
# из консоли
# из параметров командной строки при запуске
# из переменной
# Выходные данные:
# Файл groups.json в формате:
# [
#     {
#     “name”: “Название группы”,
#     “gid”: “идентификатор группы”,
#     “members_count”: количество_участников_сообщества
#     },
#     {
#     …
#     }
# ]
# Форматирование не важно, важно чтобы файл был в формате json
#
# Требования к программе:
# Программа не падает, если один из друзей пользователя помечен как “удалён” или “заблокирован”.
# Показывает что не зависла: рисует точку или чёрточку на каждое обращение к api.
# Не падает, если было слишком много обращений к API (Too many requests per second).
# Ограничение от ВК: не более 3х обращений к API в секунду.
# Могут помочь модуль time (time.sleep) и конструкция (try/except).
# Код программы удовлетворяет PEP8.
# Не использовать внешние библиотеки (vk, vkapi).
# Дополнительные требования (не обязательны для получения диплома):
# Использовать execute для ускорения работы.
# Показывает прогресс: сколько осталось до конца работы (в произвольной форме: сколько обращений к API,
# сколько минут, сколько друзей или групп осталось обработать).
# Восстанавливается если случился ReadTimeout.
# Показывать в том числе группы, в которых есть общие друзья, но не более, чем N человек,
# где N задается в коде.
# Hint: Если у пользователя больше 1000 групп, можно ограничиться первой тысячей
# Hint: Удобно использовать множества
# Материалы:
# Для того чтобы выполнить задание вам необязательно иметь аккаунт в ВК.
# Документация по методам: https://vk.com/dev/methods
# Токен для VK api:
# 73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1



from pprint import pprint
import requests
from urllib.parse import urlencode
import time
import json
delay = 0.5
APP_ID = 7304809
BASE_URL = 'https://oauth.vk.com/authorize'
auth_data = {
    'client_id': APP_ID,
    'display': 'page',
    'response_type': 'token',
    'scope': 'friends, groups',
    'v': '5.103',
}

print('?'.join((BASE_URL, urlencode(auth_data))))
# TOKEN = '4b0fa3857b3286a00b60be6a73ca3c3912327d007a62979a7ababc2d2540dfef6f6d702f84b0b3ad01ecb'
# TOKEN = '3d94296b08d61cffd60902aa32a6f47a1e0bd1d57838c320de1d1b15667127fe2a98ea56a7f57f60fe3ca'
TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
params = {
    'user_id' : id,
    'access_token': TOKEN,
    'v': '5.103'
}

class User:

    def __init__(self, id, screen_name = None, first_name = None, last_name = None):
        self.id = id
        self.id = screen_name
        self.token = TOKEN
        self.first_name = first_name
        self.last_name = last_name

    def get_params(self):
        return dict(
            access_token=self.token,
            user_id = self.id,
            v='5.103'
        )

    def get_info(self):
        params = self.get_params()
        response = requests.get(
            'https://api.vk.com/method/users.get',
            params
        )
        print('*')
        print(response.json())
        self.id = response.json()['response'][0]['id']
        self.first_name = response.json()['response'][0]['first_name']
        self.last_name = response.json()['response'][0]['last_name']
        for response.json()['response'][0] in response.json():
            print(f"https://vk.com/id{response.json()['response'][0]['id']}")
            print(self.id, self.first_name, self.last_name)
            time.sleep(delay)
        return response.json()

    def get_friends(self):
        params = self.get_params()
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params
        )
        print('**')
        return response.json()
    def print_get_friends(self):
        response = self.get_friends()
        for i in response['response']['items']:
            User(i).get_info()

    def groups_vk(self):
        params = self.get_params()
        params['extended'] = 1
        response = requests.get(
            'https://api.vk.com/method/groups.get',
            params
        )
        print('***')
        return response.json()

    def groups_vk_friends(self):
        friends = self.get_friends()
        list_groups_friends = []
        for id_friend in friends['response']['items']:
            groups = User(id_friend).groups_vk()
            if 'error' in groups:
                continue
            list_groups_friends.append(groups)
            time.sleep(delay)
        return list_groups_friends

    def id_vk_groups_friends(self):
        groups_list = self.groups_vk_friends()
        only_groups_id = []
        for group  in groups_list:
            for id_groups in group['response']['items']:
                    only_groups_id.append(id_groups['id'])
                    print(f"работает на id{id_groups['id']}")
                    time.sleep(delay)
        return only_groups_id

    def unique_groups(self):
        groups_friends = set(self.id_vk_groups_friends())
        print('*****')
        my_groups = self.groups_vk()

        my_groups_id = []
        for id_groups in my_groups['response']['items']:
            my_groups_id.append(id_groups['id'])
            time.sleep(delay)
        return set(my_groups_id).difference(groups_friends)

    def info_about_unique_groups(self):
        id_unique_groups = list(self.unique_groups())
        info_about_group = []
        for id_group in id_unique_groups:
            params = {'group_id': id_group,
                      'fields': 'members_count',
                      'access_token': TOKEN,
                      'v': '5.103'
            }
            response = requests.get(
                'https://api.vk.com/method/groups.getById',
                params
            )
            info_about_group.append(response.json())
            print('+')
            time.sleep(delay)
        return info_about_group

if __name__ == '__main__':
    vladimir = User(39946498)
    svetlana = User(308475542)
    evgen = User(171691064)
    # evgen.get_info()
    evgeny = User('eshmargunov')
    # pprint(evgeny.get_info())
    # with open('groups.json', 'w', encoding='utf-8') as gr:
    #     gr.write(json.dumps(vladimir.info_about_unique_groups()))
    #
    # with open("groups.json", encoding="utf-8") as datafile:
    #     json_data = json.load(datafile)
    #     pprint(json_data, indent=2, depth=5, width=150)
    pprint(vladimir.info_about_unique_groups())
    # pprint(evgen.info_about_unique_groups())
