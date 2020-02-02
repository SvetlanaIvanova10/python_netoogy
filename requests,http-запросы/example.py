# Задача №1
# Необходимо расширить функцию переводчика так, чтобы она принимала следующие параметры:
#
# Путь к файлу с текстом;
# Путь к файлу с результатом;
# Язык с которого перевести;
# Язык на который перевести (по-умолчанию русский).
# У вас есть 3 файла (DE.txt, ES.txt, FR.txt) с новостями на 3 языках: французском, испанском, немецком.
# Функция должна взять каждый файл с текстом, перевести его на русский и сохранить результат в новом файле.
import requests
from os import getenv

API_KEY = getenv('SECRET_KEY')
API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(path_file, path_result, from_lang, to_lang='ru'):
    with open(path_file, encoding="utf8") as file:
        text = file.read()
    lang = f'{from_lang}-{to_lang}'
    params = {
        'key': API_KEY,
        'text': text,
        'lang': lang,
    }
    response = requests.get(URL, params=params)
    json_ = response.json()
    result = ''.join(json_['text'])
    with open(path_result, 'w', encoding="utf8") as result_file:
        result_file.write(result)
    return result_file


if __name__ == '__main__':
    translate_it('DE.txt', 'translate_DE.txt', 'de')
    translate_it('ES.txt', 'translate_ES.txt', 'es')
    translate_it('FR.txt', 'translate_FR.txt', 'fr')
