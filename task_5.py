if __name__ == '__main__':
    import sys

    from itertools import zip_longest

    with open(sys.argv[1], encoding='utf-8') as names:
        with open(sys.argv[2], encoding='utf-8') as hobbies:
            names_hobbies = zip_longest((' '.join(name.split(',')) for name in names), hobbies, fillvalue=None)

            with open(sys.argv[3], 'w', encoding='utf-8') as f:
                for i in names_hobbies:
                    print(f'{str(i[0]).strip()}: {str(i[1]).strip()}', file=f)
