# Следует протестировать основные функции по получению информации о документах, добавлении и удалении элементов из словаря.
import unittest
from unittest.mock import patch
import app


class Test_My_App(unittest.TestCase):
    def setUp(self):
        self.dirs, self.docs = app.update_date()
        self.error_docs = [{"type": "insurance", "number": "10006"}]
        with patch('app.update_date', return_value=(self.dirs, self.docs)):
            with patch('app.input', return_value='q'):
                app.secretary_program_start()

    def test_delete_doc(self):
        # d – (delete) – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
        before_len_docs = len(self.docs)
        before_len_dir = len(self.dirs['1'])
        with patch('app.input', return_value='2207 876234'):
            app.delete_doc()
        self.assertLess(len(self.docs), before_len_docs)
        self.assertGreater(before_len_dir, len(self.dirs['1']))

    def test_add_new_shelf(self):
        # as – (add shelf) – команда, которая спросит номер новой полки и добавит ее в перечень;
        number_shelf = len(self.dirs.keys())
        with patch('app.input', return_value='5'):
            app.add_new_shelf()
        self.assertNotEqual(number_shelf, len(self.dirs.keys()))

    def test_doc_people(self):
        # p – (people) – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
        name_doc = self.docs[2]["name"]
        with patch('app.input', return_value='10006'):
            get_name = app.get_doc_owner_name()
        self.assertEqual(name_doc, get_name)

    def test_add_new_doc(self):
        # a – (add) – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
        # имя владельца и номер полки, на котором он будет храниться.
        new_doc = self.docs
        shelf_new_doc = self.dirs
        with patch('app.input', side_effect=['100', 'passport', 'User', '3']):
            app.add_new_doc()
        self.assertEqual(self.docs, new_doc)
        self.assertEqual(self.dirs, shelf_new_doc)
        self.assertEqual(len(self.docs), len(new_doc))
        self.assertEqual(len(self.dirs), len(shelf_new_doc))

if __name__ == '__main__':
    unittest.main()
