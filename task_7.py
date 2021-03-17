if __name__ == '__main__':
    import sys
    from itertools import islice
    with open('bakery.csv', 'r+', encoding='utf-8') as f:
        bakery = (line for line in f)
        bakery = (islice(bakery, int(sys.argv[1]) - 1, int(sys.argv[1])))
        f.seek(f.tell())
        f.write(f'{sys.argv[2]}\n')