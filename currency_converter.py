from currency import Currency


class UnknownCurrencyError(Exception):
    pass


class CurrencyConverter:
    def __init__(self, rates):
        self.rates = rates

    def convert(self, currency, to_code):
        if to_code not in self.rates:
            raise UnknownCurrencyError
        else:
            return currency * self.rates[to_code]


converter = CurrencyConverter({'USD': 1.0, 'EUR': 0.5, 'JPY': 120} )

currency = Currency('$', 4.23)

print(currency)

converted_currency = converter.convert(currency, 'USD')

print(converted_currency)
