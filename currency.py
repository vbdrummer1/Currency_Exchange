import re

class DifferentCurrencyCodeError(Exception):
    pass

class UnsupportedOperationError(Exception):
    pass

class Currency:
    def __init__(self, symbol, value):
        self.symbol = re.sub(r'[^$€¥]', '', symbol)
        self.value = value
        # self.value = re.sub(r'[0-9.,]', '', str(value))

    def __str__(self):
        return self.symbol + str(self.value)

    def __eq__(self, other):
        return self.symbol == other.symbol and self.value == other.value

    def __add__(self, other):
        if isinstance(b, Currency):
            if self.symbol != other.symbol:
                raise DifferentCurrencyCodeError
            else:
                return(Currency(self.symbol, self.value + other.value))
        else:
            print("That is not a valid input. Check your currency or number value")

    def __sub__(self, other):
        if self.symbol != other.symbol:
            raise DifferentCurrencyCodeError
        else:
            if isinstance(b, Currency):
                result = (float(self.value) - float(other.value))
                print(result)
            else:
                print("That is not a valid input. Check your currency or number value")

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Currency(self.symbol, float(self.value) * other)
        else:
            raise UnsupportedOperationError

# a = Currency('$', 3.23)
b = Currency('$', 2.00)
c = Currency('$', 5.00)
d = 3


print(b * d)
