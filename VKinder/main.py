from pprint import pprint
import requests
from urllib.parse import urlencode
import time
import json
from datetime import datetime
import random

APP_ID = 7304809
BASE_URL = 'https://oauth.vk.com/authorize'
auth_data = {
    'client_id': APP_ID,
    'display': 'page',
    'response_type': 'token',
    'scope': 'friends, photos, groups',
    'v': '5.103',
}
print('?'.join((BASE_URL, urlencode(auth_data))))
TOKEN = '3a6eeb2f3a7c9d90a860c8ca342b1c68aa43322bee3921d729c9eb858a0c74260877c526990bd2ef342a2'
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


    def print_answer(self, response):
        self.id_user = response.json()['response'][0]['id']
        self.first_name = response.json()['response'][0]['first_name']
        self.last_name = response.json()['response'][0]['last_name']
        self.interests = response.json()['response'][0]['interests']
        self.sex = response.json()['response'][0]['sex']
        self.movies = response.json()['response'][0]['movies']
        self.music = response.json()['response'][0]['music']
        self.bdate = response.json()['response'][0]['bdate']
        self.city = response.json()['response'][0]['city']
        self.books = response.json()['response'][0]['books']
        # print(f'Поиск пары для пользователя: {self.first_name} {self.last_name} ')
        # print(f'Ссылка на страницу в ВК: https://vk.com/id{self.id_user}')
        # print(f'Параметры пользователя:\n\
        #        дата рождения:{self.bdate},\n\
        #        пол(1-Ж, 2-М): {self.sex},\n\
        #        город: {self.city},\n\
        #        интересы: {self.interests},\n\
        #        любымые фильмы: {self.movies},\n\
        #        любимая музыка: {self.music},\n\
        #        любимые книги: {self.books}')
        time.sleep(delay)
        return self.interests, self.sex, self.movies, self.movies, self.music, self.bdate, self.city, self.books

    def get_params(self):
            return dict(
                access_token=self.token,
                user_id=self.id_user,
                fields=f"{'interests'}, {'sex'}, {'movies'}, {'music'}, {'bdate'}, {'city'}, {'books'}",
                v='5.103'
            )


    def get_info(self):
        params_for_det_info = self.get_params()
        response = requests.get(
            'https://api.vk.com/method/users.get',
            params_for_det_info
        )
        # print(response.json())
        self.print_answer(response)
        return response.json()

    def get_params_for_pair(self):
        params = self.get_info()
        if 'city' not in params['response'][0]:
            city = int((input("Введите id города")))
        else:
            city = params['response'][0]['city']['id']
        status = 1
        if self.bdate[5:] == '':
            bdate = int((input("Введите год рождения: ")))
        else:
            bdate = int(self.bdate[5:])
        if self.sex == 1:
            sex = 2
            age_from = datetime.today().year - bdate
            age_to = datetime.today().year - bdate + 5
        elif self.sex == 2:
            sex = 1
            age_from = datetime.today().year - bdate - 5
            age_to = datetime.today().year - bdate
        # movies = self.movies
        # music = self.music
        # interests = self.interests
        # books = self.books
        return dict(
            access_token=self.token,
            city = city,
            sex = sex,
            age_from = age_from,
            age_to = age_to,
            status = status,
            count = 1000,
            has_photo = 1,
            fields=f"{'interests'}, {'sex'}, {'movies'}, {'music'}, {'bdate'}, {'city'}, {'books'}",
            v='5.103'
        )

    def find_pair(self):
        params_for_det_info = self.get_params_for_pair()
        response = requests.get(
            'https://api.vk.com/method/users.search',
            params_for_det_info
        )
        return response.json()

    def get_id_pair(self):
        pair = self.find_pair()
        id_pair = []
        for p in pair['response']['items']:
            id_pair.append(p['id'])
        id_pair_string = ','.join(map(str,id_pair))
        # print(id_pair_string)
        return id_pair

    def common_friends(self):
        params = self.get_params()
        params['source_uid'] = self.id_user
        # id_friends = self.unique_groups()
        id_friends = self.get_id_pair()
        list_by_sort = []
        try:
            for friend in id_friends:
                params['target_uids'] = friend
                response = requests.get(
                    'https://api.vk.com/method/friends.getMutual',
                    params
                )
                time.sleep(delay)

                list_by_sort.append(response.json()['response'][0])
        except:
            print('Ошибка.')
        list_by_sort.sort(key=lambda dictionary: dictionary['common_count'], reverse=True)
        # pprint(list_by_sort)
        id_friend = []
        for friend in list_by_sort:
            id_friend.append(friend['id'])
        id_friends_string = ','.join(map(str, id_friends[:10]))
        return id_friend[:10]

    def get_photos(self):
        id_candidats = self.common_friends()
        list_photo = []
        # id_candidats = [118590263, 7962553, 27696402, 42509566, 102339502, 32066447, 26611814, 21834080, 153220338, 30756166]
        params['extended'] = 1
        params['count'] = 1000
        params['album_id'] = 'profile'
        for candidate in id_candidats:
            params['owner_id'] = candidate
            response = requests.get(
                'https://api.vk.com/method/photos.get',
                params
            )
            time.sleep(delay)

            try:
                photos_dict = dict()
                for photo in response.json()['response']['items']:
                    likes = photo['likes']['count']
                    url = photo['sizes'][-1]['url']
                    photos_dict[url] = likes
                top3_photos = sorted(photos_dict.items(), key=lambda x: x[1], reverse=True)[:3]
                link_photo = []
                for top3 in top3_photos:
                    link_photo.append(top3[0])
                list_photo.append(link_photo)
                # print(f'Топ 3 фото для https://vk.com/id{candidate}, {top3_photos}')
            except Exception:
                # print('У данного пользователя закрытый профиль.')
                list_photo.append('Ошибка. Невозможно добавить фото.')
        return list_photo, id_candidats


    def results(self):
        list_photo, id_candidats = self.get_photos()
        results = {}
        candidates = []
        for id_name, photo in zip(id_candidats, list_photo):
            params['user_id'] = id_name
            response = requests.get(
                'https://api.vk.com/method/users.get',
                params
            )
            results['id'] = response.json()['response'][0]['id']
            results['first_name'] = response.json()['response'][0]['first_name']
            results['last_name'] = response.json()['response'][0]['last_name']
            results['link'] = f"https://vk.com/id{response.json()['response'][0]['id']}"
            results['photos'] = str(photo)
            result_for_append = results.copy()
            candidates.append(result_for_append)
            results.clear()
            time.sleep(delay)
        pprint(candidates)
        return candidates

    def write_file_results(self):
        with open('candidates.json', 'w', encoding='utf-8') as gr:
            gr.write(json.dumps(self.results))


def open_json_file(file):
    with open(file, encoding="utf-8") as datafile:
            json_data = json.load(datafile)
            pprint(json_data)

if __name__ == '__main__':
    sveta = User(308475542)
    # sveta.write_file_results()
    # print(sveta.find_pair())
    sveta.results()
    # open_json_file('candidates.json')
