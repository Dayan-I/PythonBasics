class OnlyDigit(Exception):
    def __init__(self, txt):
        self.txt = txt


new_list = []

while True:
    a = input('Enter an element:')
    if a == 'stop':
        break
    else:
        try:
            if a.isdigit():
                new_list.append(a)
            elif a == 'stop':
                break
            else:
                raise OnlyDigit('List can contain only numbers')
        except (OnlyDigit) as err:
            print(err)

print(new_list)
