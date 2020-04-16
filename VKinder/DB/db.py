import psycopg2 as pg
import json


def create_db():
    with pg.connect("dbname = vkinder user = test password = 1234") as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS vkinder_candidates (
                        id serial PRIMARY KEY,
                        first_name varchar(50) NOT NULL,
                        last_name varchar(50) NOT NULL,
                        link varchar(50) UNIQUE NOT NULL,
                        photos varchar NOT NULL)""")




def add_candidate(candidate):
    with pg.connect("dbname = vkinder user = test password = 1234") as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute("""
                   INSERT into vkinder_candidates (id, first_name, last_name, link, photos) 
                   values (%s, %s, %s, %s, %s) 
                   returning id  
                   """, (candidate['id'], candidate['first_name'],
                         candidate['last_name'], candidate['link'], candidate['photos']))
                print(candidate)
                cursor.fetchone()
            except Exception:
                print('Такой id существует в базе')


def write_in_bd(name_file):
    with open(name_file, encoding="utf-8") as datafile:
        json_data = json.load(datafile)
        for candidate in json_data:
            add_candidate(candidate)


if __name__ == '__main__':
    create_db()
    write_in_bd('candidates.json')