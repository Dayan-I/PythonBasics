class ZeroDev(Exception):
    def __init__(self, txt):
        self.txt = txt



try:
    a = int(input('Enter dividend:'))
    b = int(input('Enter divider:'))
    if b == 0:
        raise ZeroDev('Divider can not be 0')
except (ValueError, ZeroDev) as err:
    print(err)
else:
    print(a / b)
