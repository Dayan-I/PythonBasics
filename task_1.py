class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def date_creator(cls, date_str):
        try:
            day, month, year = map(int, date_str.split('-'))
            date_1 = cls(day, month, year)
            return date_1
        except ValueError as err:
            print("Input numbers only")

    @staticmethod
    def validator(obj):
        if obj.day < 32 and obj.month < 13 and obj.year < 3000:
            return 'Date is valid'
        else:
            return 'Date is invalid'


mc = Date.date_creator('36-12-2067')
print(Date.validator(mc))
