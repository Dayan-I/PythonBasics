tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]


def name_class(x, y):
    for i in range(len(x)):

        for j in range(1):
            if i >= len(klasses):
                a = (x[i], None)


            else:
                a = (x[i], y[i])
        yield a


print(*name_class(tutors, klasses))
