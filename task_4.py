def val_checker(_func):
    def _val_checker(func):
        def wrapper(n):
            if _func(n):
                print(func(n))
            else:
                raise ValueError(f'wrong val {n}')
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


try:
    a = calc_cube(-5)
except ValueError as err:
    print(err)
