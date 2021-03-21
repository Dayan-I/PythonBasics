from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        new_list = [i for i in (*args, *kwargs)]
        a = [f'{func.__name__}({i}:{type(i)})' for i in new_list]
        print(*a, *func(*args, **kwargs), sep='\n' )

    return wrapper


@type_logger
def calc_cube(*args, **kwargs):
    new_list = [i for i in (*args, *kwargs.values()) if isinstance(i, int) or isinstance(i, float)]
    return [i ** 3 for i in new_list]


a = calc_cube(5, 7)
