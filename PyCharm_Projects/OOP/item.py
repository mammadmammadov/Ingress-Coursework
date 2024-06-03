import csv


class Item:
    pay_rate = 0.8

    all = []

    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than 0"
        assert quantity > 0, f"Quantity {quantity} is not greater than 0"

        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.total_price = self.__calculate_total_price()
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    def __calculate_total_price(self):
        return self.__price * self.__quantity

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
        self.total_price = self.__calculate_total_price()

    def __repr__(self):
        return f"{self.__class__.__name__}:({self.name}, {self.__price}, {self.__quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        return False

    @property
    def read_only_name(self):
        return "AAA"

    # with abstraction, we make connect and prepare_body private to hide access to them from instances since that's
    # not necessary
    def __connect(self, smtp_server):
        pass

    def __prepare_body(self):
        return f'We have {self.__name} {self.__quantity} times!'

    def send_email(self):
        self.__connect()
        self.__prepare_body()
