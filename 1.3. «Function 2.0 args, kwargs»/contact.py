from pprint import pprint

class Contact:
    def __init__(self, name, surname, *phone, favorite = False, **info):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.favorite = favorite
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
        contact_info = f'Имя: {self.name},\n' \
                f'Фамилия: {self.surname},\n' \
                f'Телефон: {self.phone},\n' \
                f'В избранных: {self.favorite},\n' \
                f'Дополнительная информация: {self.info}'
        return contact_info



# class PhoneBook:
#
#     def __init__(self,name_book):
#         self.name_book = name_book
#         self.contact = None
#     def print_contact(self):
#         return self.contact
if __name__ == '__main__':

    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    print(jhon)
#
# book1 = PhoneBook('bvz')
# print(book1.print_contact())
# print(book1)
