from market import Market

m = Market()

class Portfolio:
    def __init__(self, holdings, cash):
        self.holdings = holdings
        self.cash = cash

    def buy(self, stock_name, quantity):
        stock = m.get_stock(stock_name)
        if (stock):
            total = stock.price * quantity
            if (0 < total <= self.cash):
                self.cash -= total
                self.holdings.append((stock_name, quantity))
                return True
        return False

    def sell(self, stock_name, quantity):
        print(stock_name, self.holdings)
        for holding in self.holdings:
            if stock_name in holding:
                if quantity <= holding[1]:
                    return True
        return False

    def __repr__(self):
        print("Holdings:")
        for stock in self.holdings:
            print(stock[1], "shares of", stock[0])
        
        print("Cash:", self.cash)