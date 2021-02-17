duration = int(input('Enter time in seconds : '))


if duration < 60:
    print(duration % 60, 'сек')
elif 60 <= duration < 3600:
     print(duration // 60, 'мин',duration % 60, 'сек')
elif 3600 <= duration < 86400:
    print (duration // 3600, 'час', (duration % 3600) // 60, 'мин',duration % 60, 'сек' )
elif 86400 <= duration:
    print (duration // 86400, 'дн', (duration % 86400) // 3600, 'час', (duration % 3600) // 60, 'мин',duration % 60, 'сек' )

# можно использовать и цикл для проверки сразу нескольких значений, предварительно упаковав их в список
durations = (input('Enter more than one duration : ')).split() # вводим значения, но пока не делаем их int
list(durations)  # создаём список
print(durations)# проверяем спискок, все ок
list_1 =[] # созадаём пустой список и добавляем туда элементы предыдущего массива, но уже сделав их int
for i in durations:
    i = int(i)
    list_1.append(i)
print(list_1)

for i in list_1:

    if i < 60:
        print(i % 60, 'сек')
    elif 60 <= i < 3600:
        print(i // 60, 'мин', i % 60, 'сек')
    elif 3600 <= i < 86400:
        print(i // 3600, 'час', (i % 3600) // 60, 'мин', i % 60, 'сек')
    elif 86400 <= i:
        print(i // 86400, 'дн', (i % 86400) // 3600, 'час', (i % 3600) // 60, 'мин', i % 60,
              'сек')
