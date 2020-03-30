import requests

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def get_params(text,with_lang, to_lang):
    return {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(with_lang, to_lang),
    }
def translate_it(text,with_lang, to_lang):
    params = get_params(text,with_lang, to_lang)
    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])

if __name__ == '__main__':
    print(translate_it('hi','en', 'ru'))