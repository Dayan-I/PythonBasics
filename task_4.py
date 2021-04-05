class Store:
    def __init__(self):
        self.store = {}

    def to_receive(self, obj):
        if obj.model not in self.store.keys():
            self.store.setdefault(obj.model, obj.quantity)
        else:
            self.store[obj.model] += obj.quantity


class OrgTech:
    def __init__(self, model, cost, quantity):
        self.model = model
        self.cost = cost
        self.quantity = quantity


class Printer(OrgTech):
    def __init__(self, model, cost, quantity, color):
        self.color = color
        super().__init__(model, cost, quantity)


class Scanner(OrgTech):
    def __init__(self, model, cost, quantity, type):
        self.type = type
        super().__init__(model, cost, quantity)


class Xerox(OrgTech):
    def __init__(self, model, cost, quantity, mobility):
        self.mobility = mobility
        super().__init__(model, cost, quantity)


a = Printer('Samsung', 1000, 3, 'multi')
c = Printer('Samsung', 1000, 5, 'multi')
b = Store()
b.to_receive(a)
b.to_receive(c)
print(b.store)


