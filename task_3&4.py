names = 'Иван', 'Петя', 'Илья', 'Мария', 'Миша', 'Инга'


def thesaurus(x):
    new_dict = {}
    for i in x:
        a = i[0]
        if i.startswith(a) and a not in new_dict.keys():
            new_list = list()
            new_list.append(i)
            new_dict[a] = new_list
        elif a in new_dict.keys() and i.startswith(a):
            new_dict[a].append(i)
    k = sorted(new_dict.keys())
    for i in k:
        print(f"{i}: {new_dict[i]}")


thesaurus(names)

# Третье задание
names_surnames = 'Иван Сергеев', 'Петя Мальцов', 'Илья Муромец', 'Мария Шукшина', 'Миша Пупкин', 'Инга Савина'


def thesaurus_adv(x):
    new_dict = {}

    for i in x:
        surname = i.split(' ')
        name = surname[0]
        surname = surname[1]
        str(name)
        str(surname)
        a = surname[0]
        b = name[0]
        new_dict_1 = dict()
        if surname.startswith(a) and a not in new_dict.keys():

            new_list = list()
            new_list.append(i)
            new_dict_1[b] = new_list
            new_dict[a] = new_dict_1

        elif a in new_dict.keys() and surname.startswith(a) and b not in new_dict[a].keys():
            new_dict[a].setdefault(b, i)
        elif name.startswith(b) and a in new_dict.keys() and surname.startswith(a):
            new_dict[a][b].append(i)
    k = sorted(new_dict.keys())
    for i in k:
        print(f"{i}: {new_dict[i]}")




thesaurus_adv(names_surnames)
