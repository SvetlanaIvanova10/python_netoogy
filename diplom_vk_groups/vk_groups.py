# Вывести список групп в ВК в которых состоит пользователь, но не состоит никто из его друзей.
# Токен для VK api:
# 73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1
from pprint import pprint
import requests
from urllib.parse import urlencode
import time
import json

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
TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
params = {
    'user_id' : id,
    'access_token': TOKEN,
    'v': '5.103'
}
delay = 0.5
class User:

    def __init__(self, id_user = None, screen_name = None, first_name = None, last_name = None):
        if type(id_user) != str:
            self.id_user = id_user
        else:
            self.id_user = screen_name
        self.token = TOKEN
        self.first_name = first_name
        self.last_name = last_name

    def get_params(self):
        return dict(
            access_token=self.token,
            user_id = self.id_user,
            v='5.103'
        )

    def get_info(self):
        params_for_det_info = self.get_params()
        response = requests.get(
            'https://api.vk.com/method/users.get',
            params_for_det_info
        )
        print('*')
        print(response.json())
        self.id_user = response.json()['response'][0]['id']
        self.first_name = response.json()['response'][0]['first_name']
        self.last_name = response.json()['response'][0]['last_name']
        for response.json()['response'][0] in response.json():
            print(f"https://vk.com/id{response.json()['response'][0]['id']}")
            print(self.id_user, self.first_name, self.last_name)
            time.sleep(delay)
        return response.json()

    def groups_vk(self):
        params_for_groups_vk = self.get_params()
        response = requests.get(
            'https://api.vk.com/method/groups.get',
            params_for_groups_vk
        )

        print('***')
        return response.json()

    def unique_groups(self):
        groups = self.groups_vk()
        list_groups =[]
        try:
            for group in groups['response']['items']:
                params_for_group = {
                    'filter': 'friends',
                    'group_id': group,
                    'access_token': TOKEN,
                    'v': '5.103'
                }
                response = requests.get(
                    'https://api.vk.com/method/groups.getMembers',
                    params_for_group
                )

                print('++')
                time.sleep(delay)
                if response.json()['response']['count'] == 0:
                    list_groups.append(group)
                else:
                    continue
        except Exception:
            print('Что-то пошло не так')
            print(Exception)
        return list_groups

    def info_about_unique_groups(self):
        id_unique_groups = self.unique_groups()
        info_about_group = []
        for id_group in id_unique_groups:
            params_for_id_group = self.get_params()
            params_for_id_group['group_id'] = id_group
            params_for_id_group['fields'] = 'members_count'
            response = requests.get(
                'https://api.vk.com/method/groups.getById',
                params_for_id_group
            )
            info_about_group.append(response.json()['response'])
            print('+')
            time.sleep(delay)
        return info_about_group

if __name__ == '__main__':
    evgen = User(171691064)
    evgeny = User('eshmargunov')
    with open('groups.json', 'w', encoding='utf-8') as gr:
        gr.write(json.dumps(evgeny.info_about_unique_groups()))
    with open("groups.json", encoding="utf-8") as datafile:
        json_data = json.load(datafile)
        pprint(json_data, indent=2, depth=5, width=150)
