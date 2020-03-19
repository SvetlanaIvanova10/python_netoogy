# from contact import Contact
import sys
from pprint import pprint
import json
class Contact:
    def __init__(self, name, surname, *phone, favorite = False, **info,):
        self.name = name
        self.surname = surname
        self.favorite = favorite
        self.phone = phone

        self.info = info

    def dir_contact(self):
        return dict(name = self.name,
        surname= self.surname,
        phone= self.phone,
        favorite= self.favorite,
        info=self.info)

    # def __str__(self):
    #     book = self.dir_contact()
    #     book1 = f'Имя: {book["name"]},\n' \
    #             f'Фамилия: {book["surname"]},\n' \
    #             f'Телефон: {book["phone"]},\n' \
    #             f'В избранных: {book["favorite"]},\n' \
    #             f'Дополнительная информация: {book["info"]}'
    #     return book1
    def __str__(self):
        return f'Имя: {self.name},\n' \
                f'Фамилия: {self.surname},\n' \
                f'Телефон: {self.phone},\n' \
                f'В избранных: {self.favorite},\n' \
                f'Дополнительная информация: {self.info}'
        # contact_info = {'Имя': self.name,
        #  'Фамилия': self.surname,
        #  'Телефон': self.phone,
        #  'В избранных': self.favorite,
        #  'Дополнительная информация': self.info}



class PhoneBook:

    def __init__(self,name_book):
        self.name_book = name_book
        self.contacts = []


    def add_contact(self, *contact_name):
        self.contacts.extend(contact_name)

    def print_contacts(self):
        print(self.name_book)
        for cont in self.contacts:
            print(cont)

    def del_contact(self, del_cont):
        for contact in self.contacts:
            for iter_phone in contact.phone:
                if iter_phone == del_cont:
                    self.contacts.remove(contact)
                    print('Контакт удален')


    def found_favorites(self):
        print('Избранные контакты:')
        for contact in self.contacts:
            if contact.favorite == True:
                print(contact)

    def found_contact(self, name, surname):
        print('Поиск контакта по имени и фамилии:')
        for contact in self.contacts:
            if contact.name == name and contact.surname == surname:
                print(contact)


def adv_print(*objects, start = '\n', max_line = 10, in_file=False,**kwargs):

    def print_output(max_line):
        print(start)
        for obj in objects:
            if len(obj) >= max_line:
                for i in range(0, len(obj), max_line):
                    print(obj[i:max_line])
                    max_line += max_line
            else:
                print(obj)

    if in_file != False:
        with open('test.txt', 'w') as test_file:
            sys.stdout = test_file
            print_output(max_line)
    else:
        print_output(max_line)









if __name__ == '__main__':
    jhon = Contact('Jhon', 'Smith',  '+71234567829',favorite = True, telegram='@jhony', email='jhony@smith.com')
    vlad = Contact('vlad', 'Smithon', '+71234567809', telegram='@jho', email='jhony@smithon.com')
    vladic = Contact('vladic', 'Smit', '+71234566809',favorite = True, telegram='@jho', email='jhony@smithon.com')

    book = PhoneBook('bvz')
    book.add_contact(jhon, vlad)
    book.print_contacts()
    print()
    book.add_contact(vladic)
    book.print_contacts()
    book.del_contact('+71234566809')
    print()
    book.print_contacts()
    print()
    book.found_favorites()
    print()
    book.found_contact('vladic', 'Smit')
    print()
    book.found_contact('vlad', 'Smithon')
    adv_print('12345678901234567891234567', '1235', in_file=True, start='start')

