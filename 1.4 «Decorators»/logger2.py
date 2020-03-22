# Написать декоратор из п.1, но с параметром – путь к логам.
import logging
from functools import wraps


def info_decorator(func):
    @wraps(func)
    def info_about_func(*argv, **kwargv):
        my_file = input('введите название файла для записи логгера (без формата): ')
        format = f'%(levelname)s [%(asctime)s] %(message)s'
        logging.basicConfig(format = format,
                            level = logging.DEBUG,
                            filename = f'{my_file}.log',
                            filemode = 'w')
        result = func(*argv, **kwargv)
        logging.info(
            f"имя функции: {func.__name__}, аргументы: {argv},{kwargv}, возвращаемое значение: {result}")
        return func(*argv, **kwargv)
    return info_about_func


if __name__ == '__main__':
    @info_decorator
    def plus(a, b):
        result = a + b
        return result

    print(plus(4,6))