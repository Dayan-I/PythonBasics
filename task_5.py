new_list = [1.1, 2.22, 3.00, 10.31, 46.57, 79.99, 32.01, 22.83, 15.20, 50]
a = ' '
for i in new_list:
    if i % 1 < 0.10:
        i = f'{int(i // 1):02d} руб 0{((i % 1) * 100):.0f} коп '
    else:
        i = f'{int(i // 1):02d} руб {((i % 1)*100):.0f} коп '
    a += i
print(a)
print(id(new_list))
new_list.sort()
print(id(new_list), new_list)
new_list_sorted = sorted(new_list, reverse=True)
print(new_list_sorted)

_most_expensive = []
a = len(new_list)
for i in new_list:
    _most_expensive.append(new_list.pop())
    while new_list.index(i) >= a - 5: break
print(sorted(_most_expensive))