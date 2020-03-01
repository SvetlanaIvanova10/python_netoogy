from application.db import people
from application import salary
from datetime import datetime

if __name__ == '__main__':
    print(f'Зарплата {people.get_employees()} : {salary.calculate_salary()}')
    print(datetime.now())