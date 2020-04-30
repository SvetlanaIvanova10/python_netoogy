import itertools
import psycopg2 as pg
import json
from DB.config import connector

class ConnBD:
    def __init__(self):
        self.info_db = connector
        self.conn = pg.connect(self.info_db)
        self.cursor = self.conn.cursor()

    def query(self, request, param = None):
        self.cursor.execute(request, param)
        self.conn.commit()

    def fetch(self):
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()

class UserBD:
    def __init__(self):
        self.cursor = ConnBD()

    def create_db(self):
        request = f"""
                    CREATE TABLE IF NOT EXISTS vkinder_candidates (
                            id serial PRIMARY KEY,
                            first_name varchar(50) NOT NULL,
                            last_name varchar(50) NOT NULL,
                            link varchar(50) UNIQUE NOT NULL,
                            photos varchar NOT NULL)"""
        self.cursor.query(request)
        # with pg.connect(connector) as conn:
        #     with conn.cursor() as cur:
        #         cur.execute("""
        #             CREATE TABLE IF NOT EXISTS vkinder_candidates (
        #                     id serial PRIMARY KEY,
        #                     first_name varchar(50) NOT NULL,
        #                     last_name varchar(50) NOT NULL,
        #                     link varchar(50) UNIQUE NOT NULL,
        #                     photos varchar NOT NULL)""")

    def add_candidate(self, candidate):
        # with pg.connect("dbname = vkinder user = test password = 1234") as conn:
        #     with conn.cursor() as cur:
        try:
            request = f"""
                   INSERT into vkinder_candidates (id, first_name, last_name, link, photos)
                   values (%s, %s, %s, %s, %s)
                   returning id
                   """
            param = candidate['id'], candidate['first_name'], candidate['last_name'], candidate['link'], candidate['photos']
            self.cursor.query(request,param)
                    # cur.execute("""
                    #    INSERT into vkinder_candidates (id, first_name, last_name, link, photos)
                    #    values (%s, %s, %s, %s, %s)
                    #    returning id
                    #    """, (candidate['id'], candidate['first_name'],
                    #          candidate['last_name'], candidate['link'], candidate['photos']))
                    # print(candidate)
                    # cur.fetchone()
            self.cursor.fetch()
        except Exception as e:
            print('Ошибка', e)

    def chech_id(self, id_user):
        request = f"""
                       SELECT id FROM vkinder_candidates
                       """
        self.cursor.query(request)
        row = self.cursor.fetch()
        if (id_user in itertools.chain(*row)) :
            return 1
        else:
            return 0
    #
    # def write_in_bd(self, name_file):
    #     with open(name_file, encoding="utf-8") as datafile:
    #         json_data = json.load(datafile)
    #         for candidate in json_data:
    #             self.add_candidate(candidate)


if __name__ == '__main__':

    db = UserBD()
    # db.create_db()
    #
    # r={'id': '9576005', 'first_name': 'Katie','last_name': 'Smith', 'link': 'https://vk.id61', 'photos': '123'}
    # db.add_candidate(r)
    #
    print(db.chech_id(95765))