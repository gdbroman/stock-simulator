from stock import Stock


class Market:
    def __init__(self):
        self.stocks = [
            Stock("TSLA", 100),
            Stock("GOOGLE", 200)
        ]

    def get_stock(self, stock_name):
        for stock in self.stocks:
            if stock.name == stock_name:
                return stock
        return False