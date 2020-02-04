# Вам предстоит решить задачу поиска общих друзей у пользователей VK.
# Задача №1
# Пользователя нужно описать с помощью класса и реализовать метод поиска общих друзей, используя API VK.
#
# Задача №2
# Поиск общих друзей должен происходить с помощью оператора &, т.е. user1 & user2
# должен выдать список общих друзей пользователей user1 и user2, в этом списке должны быть экземпляры классов.
#
# Задача №3
# Вывод print(user) должен выводить ссылку на профиль пользователя в сети VK
from pprint import pprint
import requests
from urllib.parse import urlencode
import time
APP_ID = 7304809
BASE_URL = 'https://oauth.vk.com/authorize'
auth_data = {
    'client_id': APP_ID,
    'display': 'page',
    'response_type': 'token',
    'scope': 'friends',
    'v': '5.103',
}

print('?'.join((BASE_URL, urlencode(auth_data))))
TOKEN = '4cdb838e309863b52aed05a2ceccd513647cd878bc29bb9a58ca3bf4d68bf06bf2de68d7a4c8f53c6693e'

params = {
    'user_id' : id,
    'access_token': TOKEN,
    'v': '5.103'
}

class User:

    def __init__(self, id, first_name=None, last_name=None):
        self.id = id
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
        for response.json()['response'][0] in response.json():
            print(f"https://vk.com/id{response.json()['response'][0]['id']}")
            print(response.json()['response'][0]['id'],\
                  response.json()['response'][0]['first_name'],\
                  response.json()['response'][0]['last_name'])
            time.sleep(1)
        # self.id = response.json()['response'][0]['id']
        # self.first_name = response.json()['response'][0]['first_name']
        # self.last_name = response.json()['response'][0]['last_name']
        return response.json()

    def get_friends(self):
        params = self.get_params()
        params['fields'] = 'first_name'
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params
        )
        for i in response.json()['response']['items']:
            print(f'https://vk.com/id{i["id"]}')
            print(i['id'], i['first_name'], i['last_name'])
        # return response.json()

    def __and__(self, user):
        params['source_uid'] = self.id
        params['target_uid'] = user.id
        response = requests.get(
            'https://api.vk.com/method/friends.getMutual',
            params
        )
        print('Общие друзья:')
        for i in response.json()['response']:
            user_info = User(i)
            user_info.get_info()
        # return response.json()

    def __str__(self):
        return f'https://vk.com/id{self.id}'



vladimir = User(39946498)
vladimir.get_info()
print()
vladimir.get_friends()
print()
svetlana = User(308475542)
svetlana.get_info()
print()
# svetlana.get_friends()
print()
print(User(124866996))
print(svetlana)
print()
print(svetlana & vladimir)

