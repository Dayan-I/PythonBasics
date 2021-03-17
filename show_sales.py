if __name__ == '__main__':
    import sys
    from itertools import islice

    if len(sys.argv) == 1:
        with open('bakery.csv', encoding='utf-8') as f:
            print(f.read())
    elif len(sys.argv) == 2:
        with open('bakery.csv', encoding='utf-8') as f:
            bakery = (line for line in f)
            print(*islice(bakery, int(sys.argv[1]) - 1,None))

    elif len(sys.argv) == 3:
        with open('bakery.csv', encoding='utf-8') as f:
            bakery = (line for line in f)
            print(*islice(bakery, int(sys.argv[1]) - 1, int(sys.argv[2])))
