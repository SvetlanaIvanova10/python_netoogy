from application.salary import *
from application.db.people import *
from datetime import datetime

if __name__ == '__main__':
    print(calculate_salary())
    print(get_employees())
    print(datetime.now())