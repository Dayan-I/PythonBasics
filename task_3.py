from requests import get, utils
from decimal import Decimal, getcontext
from datetime import date


def currency_rates(valute):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    if valute in content:
        _date = content[content.find('Date'):]
        _date = _date[6:]
        _date = _date[:_date.find('"')].split('.')
        _date = list(map(int, _date))
        _date = date(year=(_date[2]), month=(_date[1]), day=(_date[0]))
        content = content[content.find(valute):]
        b = 'Value'
        content = content[content.find(b):]
        content = content[content.find('>'):content.find('<')]
        content = content[1:]
        content = content.replace(',', '.')
        getcontext().prec = 4
        a = Decimal(content)
        print(f'Rate of {valute} to RUB={a}. Rate is actual on date {_date}')
    else: print(None)


valute = input('Enter the currency you want to know the rate :').upper()
currency_rates(valute)
