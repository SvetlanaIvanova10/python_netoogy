# Проверим актуальность API Яндекс.Переводчик'а для потенциального сервиса переводов.
# Используя библиотеку request напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой
# Пример положительных тестов:
# Код ответа соответствует 200
# результат перевода правильный - "привет"
import unittest
import requests
import translate


class Test_My_Trnslate(unittest.TestCase):

    def setUp(self):
        self.translate = translate.translate_it('Привет', 'ru', 'en')
        self.status = translate.get_params('Привет', 'ru', 'en')

    def test_response_status(self):
        expected_status = 200
        response_status = requests.get(translate.URL, params = self.status)
        self.assertEqual(response_status.status_code, expected_status)

    def test_invalid_status(self):
        expected_invalid_status = 400
        response_invalid_status = requests.get(translate.URL, params=self.translate)
        self.assertEqual(response_invalid_status.status_code, expected_invalid_status)

    def test_translate_word(self):
        expected = 'hi'
        self.assertEqual(self.translate.lower(), expected.lower())

if __name__ == '__main__':
    unittest.main()
