import random
import math
from stock import Stock


class Market:
    def __init__(self):
        self.stocks = [
            Stock("TSLA", 1452),
            Stock("GOOGL", 1498),
            Stock("AAPL", 445),
            Stock("FB", 268),
        ]

    def get_stock(self, stock_name):
        for stock in self.stocks:
            if stock.name == stock_name:
                return stock
        return False

    def update(self):
        for x in enumerate(self.stocks):
            index = x[0]
            stock = x[1]
            stock_name = stock.name
            old_price = stock.price
            # Normal distribution with 7% return as mean and 2% standard deviation
            new_price = math.ceil(old_price * (random.normalvariate(1.07, 0.02)))
            self.stocks[index] = Stock(stock_name, new_price)

    def __repr__(self):
        for stock in self.stocks:
            print(stock.name, stock.price)