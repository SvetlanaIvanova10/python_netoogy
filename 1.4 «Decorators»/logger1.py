# Написать декоратор - логгер.
# Он записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
import logging
from functools import wraps


def info_decorator(func):
    @wraps(func)
    def info_about_func(*argv, **kwargv):
        format = f'%(levelname)s [%(asctime)s] %(message)s'
        logging.basicConfig(format=format,
                            level=logging.DEBUG,
                            filename=f'mylog.log',
                            filemode = 'w')
        result = func(*argv, **kwargv)
        logging.info(
            f"имя функции: {func.__name__}, аргументы: {argv},{kwargv}, возвращаемое значение: {result}")
        return func(*argv, **kwargv)
    return info_about_func
