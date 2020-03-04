import hashlib


def MD5_hesh(path):
    with open(path, encoding='utf8') as name_file:
        for hesh in name_file:
            hesh = hesh.strip().replace(' ', '_')
            hash_object = hashlib.md5(hesh.encode())
            yield f'MD5 хеш строки {hesh} : {hash_object.hexdigest()}'


if __name__ == '__main__':
    for link in MD5_hesh('name_countries.list'):
        print(link)
