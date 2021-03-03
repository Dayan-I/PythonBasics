
print('I am:', __name__)
if __name__ == '__main__':
    import utils
    import sys
    print(currency_rates(str(sys.argv[1])))
