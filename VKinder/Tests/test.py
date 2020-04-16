import unittest
import requests
import main


class Test_My_Class(unittest.TestCase):
    def setUp(self):
        self.user = main.User(308475542)

    def test_get_params(self):
         expected_response = {
            "response": [{
            "id": 308475542,
            "first_name": "Света",
            "last_name": "Иванова",
            "is_closed": False,
            "can_access_closed": True,
            "sex": 1,
            "bdate": "2.10.1997",
            "city": {
                "id": 122,
                "title": "Рязань"
            },
            "interests": "",
            "music": "рок, альтернатива",
            "movies": "Гарри Поттер, Доктор Кто, Чужестранка",
            "books": "Гарри Поттер"
            }]
         }
         self.info = self.user.get_info()
         self.assertEqual(self.info, expected_response)

    def test_find_pair_response_status(self):
        expected_status = 200
        response_status = requests.get(main.BASE_URL,params = main.auth_data)
        self.assertEqual(response_status.status_code, expected_status)

    def test_find_pair_response_status_invalid(self):
        expected_status = 200
        response_status = requests.get(main.BASE_URL,params = main.params)
        self.assertNotEqual(response_status.status_code, expected_status)

    def test_type_get_id_pair(self):
        expected_type = list
        get_type = type(self.user.get_id_pair())
        self.assertEqual(expected_type, get_type)

    def test_get_params_for_pair(self):
        expected_len = ['access_token', 'city', 'sex', 'age_from',
                        'age_to', 'status', 'count', 'has_photo', 'fields', 'v']
        len_dict = self.user.get_params_for_pair().keys()
        self.assertCountEqual(len_dict, expected_len)



if __name__ == '__main__':
    unittest.main()
