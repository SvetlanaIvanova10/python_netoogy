# Написать декоратор из п.1, но с параметром – путь к логам.
import logging
from functools import wraps

def param_info_decorator(name_file):
    def info_decorator(func):
        @wraps(func)
        def info_about_func(*argv, **kwargv):
            format = f'%(levelname)s [%(asctime)s] %(message)s'
            logging.basicConfig(format = format,
                                level = logging.DEBUG,
                                filename = name_file,
                                filemode = 'w')
            result = func(*argv, **kwargv)
            logging.info(
                f"имя функции: {func.__name__}, аргументы: {argv},{kwargv}, возвращаемое значение: {result}")
            return func(*argv, **kwargv)
        return info_about_func
    return info_decorator

if __name__ == '__main__':
    @param_info_decorator('log_file.log')
    def plus(a, b):
        result = a + b
        return result

    print(plus(4,6))