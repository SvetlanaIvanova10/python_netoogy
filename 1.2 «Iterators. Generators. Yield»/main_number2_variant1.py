import hashlib


class md5_hesh:

    def __init__(self, path):
        self.file = open(path, encoding='utf8')
        # self.session = requests.Session()

    def __iter__(self):
        return self

    def __next__(self):
        hesh = self.file.readline().strip().replace(' ', '_')
        if not hesh:
            raise StopIteration
        hash_object = hashlib.md5(hesh.encode())
        return f'MD5 хеш строки {hesh} : {hash_object.hexdigest()}'


if __name__ == '__main__':
    for link in md5_hesh('name_countries.list'):
        print(link)

