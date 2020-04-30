import operator
from collections import Counter
from pprint import pprint
import requests
from urllib.parse import urlencode
import time
import json
from datetime import datetime
from DB.db import UserBD

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
TOKEN = '0c48ede1fedb990ce3bb7c8e7c8b3e157c8cbe2f3ce724db311317afc4ed5c6f7af37f91e2bb5d4de805c'
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

    def response(self, metod, parametrs):
        try:
            response = requests.get(
                f'https://api.vk.com/method/{metod}',
                parametrs
            )
            return response.json()['response']
        except KeyError:
            print('Ошибка. Неправильный запроос:', response.json())

    def save_answer(self, response):
        response_data = response[0]
        self.id_user = response_data['id']
        self.first_name = response_data['first_name']
        self.last_name = response_data['last_name']
        if ('bdate' not in response_data):
            self.bdate = int((input("Введите год рождения: ")))
        else:
            if response_data['bdate'][5:] == '':
                self.bdate = int((input("Введите год рождения: ")))
            else:
                self.bdate = int(response_data['bdate'][5:])
        if 'city' not in response_data:
            self.city = int((input("Введите id города")))
        else:
            self.city = response_data['city']['id']
        self.sex = response_data['sex']
        time.sleep(delay)
        return self.sex, self.city, self.bdate

    def get_params(self):
            return dict(
                access_token=self.token,
                user_id=self.id_user,
                fields=f"{'interests'}, {'sex'}, {'movies'}, {'music'}, {'bdate'}, {'city'}, {'books'}",
                v='5.103'
            )

    def get_info(self):
        params_for_det_info = self.get_params()
        answer =  self.response('users.get', params_for_det_info)
        self.save_answer(answer)
        return answer

    def get_params_for_pair(self):
        self.get_info()
        status = 1
        if self.sex == 1:
            sex = 2
            age_from = datetime.today().year - self.bdate
            age_to = datetime.today().year - self.bdate + 5
        elif self.sex == 2:
            sex = 1
            age_from = datetime.today().year - self.bdate - 5
            age_to = datetime.today().year - self.bdate
        if self.sex == 0:
            my_sex = int(input('Какой пол будем искать? Введите 1, если женский и 2, если мужской'))
            if my_sex == 1:
                sex = 2
                age_from = datetime.today().year - self.bdate
                age_to = datetime.today().year - self.bdate + 5
            else:
                sex = 1
                age_from = datetime.today().year - self.bdate - 5
                age_to = datetime.today().year - self.bdate
        return dict(
            access_token=self.token,
            city = self.city,
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
        answer = self.response('users.search', params_for_det_info)
        filter_answer = [d for d in answer['items'] if d["is_closed"] == False]
        return filter_answer

    def get_id_pair(self):
        pair = self.find_pair()
        id_pair = []
        for p in pair:
            id_pair.append(p['id'])
        return id_pair

    def common_friends(self):
        params = self.get_params()
        params['source_uid'] = self.id_user
        id_friends = self.get_id_pair()
        list_by_sort = {}
        try:
            for friend in id_friends:
                params['target_uids'] = friend
                answer = self.response('friends.getMutual', params)
                time.sleep(delay)
                list_by_sort[answer[0]['id']] = answer[0]['common_count']
        except Exception:
            print('Ошибка.')
        return list_by_sort

    def groups_vk(self):
        params_for_groups_vk = self.get_params()
        answer = self.response('groups.get', params_for_groups_vk)
        return answer['items']

    def split_list(self, arr, size):
        arrs = []
        while len(arr) > size:
            pice = arr[:size]
            arrs.append(pice)
            arr = arr[size:]
        arrs.append(arr)
        return arrs

    def common_groups(self):
        groups = self.groups_vk()
        user_ids = self.get_id_pair()
        user_ids_split = self.split_list(user_ids, 25)
        dict_count = {}
        for id in user_ids:
            dict_count[id] = 0
        try:
            for group in groups:
                for user_id in user_ids_split:
                    user_id = ','.join(map(str, user_id))
                    params_for_group = {
                        'user_ids': user_id,
                        'group_id': group,
                        'access_token': TOKEN,
                        'v': '5.103'
                    }
                    answer = self.response('groups.isMember', params_for_group)
                    time.sleep(delay)
                    for i in answer:
                        if i['member'] == 1:
                            dict_count[i['user_id']] += 1
                        else:
                            continue

        except Exception:
            print('Что-то пошло не так')
        return dict_count

    def common_interests(self):
        interests = str(input('Введите свои интересы: '))
        books = str(input('Введите свои любимые книги: '))
        music = str(input('Введите свою любимую музыку: '))
        movies = str(input('Введите свои любимые фильмы: '))
        self.interests = (interests + ' ' + books + ' ' + music + ' ' + movies).replace(',', '').split(' ')
        interests_filter = {}
        interests_matches = {}
        users_list = self.get_id_pair()
        for uid in users_list:
            params = self.get_params()
            params['user_id'] = uid
            params['fields'] = 'interests, books, music, movies'
            user = self.response('users.get', params)
            time.sleep(delay)
            try:
                inter = (user[0]['music'] + ' ' + user[0]['interests'] + ' ' + user[0]['books']
                             ).replace(',', '').split(' ')
                interests_filter = [item for item in inter if item != '']
            except KeyError:
                print("У этого человека не интересов")
            interests_matches[uid] = len(set(self.interests).intersection(set(interests_filter)))
        return interests_matches

    def common_results(self):
        groups = self.common_groups()
        friends = self.common_friends()
        interests = self.common_interests()
        common = (friends, groups, interests)
        total_sort = Counter()
        for item in common:
            total_sort.update(item)
        total_sort = dict(total_sort)
        total_sort = sorted(total_sort.items(), key=operator.itemgetter(1), reverse=True)
        id_total_sort = []
        for iter in total_sort:
            id_total_sort.append(iter[0])
        return id_total_sort

    def chech_in_db(self):
        list_id_not_in_db = []
        id_check = self.common_results()
        for i in id_check:
            result = UserBD()
            return_result = result.chech_id(i)
            if return_result == 0:
                list_id_not_in_db.append(i)
            else:
                continue
        return list_id_not_in_db[:10]

    def get_photos(self):
        id_candidats = self.chech_in_db()
        list_photo = []
        params['extended'] = 1
        params['count'] = 1000
        params['album_id'] = 'profile'
        for candidate in id_candidats:
            params['owner_id'] = candidate
            answer = self.response('photos.get', params)
            time.sleep(delay)
            try:
                photos_dict = dict()
                for photo in answer['items']:
                    likes = photo['likes']['count']
                    url = photo['sizes'][-1]['url']
                    photos_dict[url] = likes
                top3_photos = sorted(photos_dict.items(), key=lambda x: x[1], reverse=True)[:3]
                link_photo = []
                for top3 in top3_photos:
                    link_photo.append(top3[0])
                list_photo.append(link_photo)
            except Exception:
                list_photo.append('Ошибка. Невозможно добавить фото.')
        return list_photo, id_candidats

    def results(self):
        list_photo, id_candidats = self.get_photos()
        results = {}
        candidates = []
        for id_name, photo in zip(id_candidats, list_photo):
            params['user_id'] = id_name
            answer = self.response('users.get', params)
            response_data = answer[0]
            results['id'] = response_data['id']
            results['first_name'] = response_data['first_name']
            results['last_name'] = response_data['last_name']
            results['link'] = f"https://vk.com/id{results['id']}"
            results['photos'] = str(photo)
            result_for_append = results.copy()
            candidates.append(result_for_append)
            results.clear()
            time.sleep(delay)
        return candidates

    def write_file_results(self):
        file_name = 'candidates.json'
        with open(file_name, 'w', encoding='utf-8') as gr:
            gr.write(json.dumps(self.results()))
        return file_name

    def open_json_file(self, file_name):
        with open(file_name, encoding="utf-8") as datafile:
                json_data = json.load(datafile)
                pprint(json_data)

    def write_in_bd(self):
        file_name = self.write_file_results()
        with open(file_name, encoding="utf-8") as datafile:
            json_data = json.load(datafile)
            for candidate in json_data:
                result = UserBD()
                result.add_candidate(candidate)
                print(result)
        self.open_json_file(file_name)


if __name__ == '__main__':
    sveta = User(308475542)
    sveta.write_in_bd()
    # alex = User(19165090)
    # pprint(alex.get_info())
    # alex.write_in_bd()

