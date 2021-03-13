with open('content.txt', encoding='utf-8') as f:
    content = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in f)

    new_dict = {}
    for i in content:
        if i[0] in new_dict.keys():
            new_dict[i[0]] += 1
        else:
            new_dict.setdefault(i[0], 1)
    for k in new_dict.keys():
        if new_dict[k] == max(new_dict.values()):
            print(k, new_dict[k])


