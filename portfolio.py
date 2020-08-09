from market import Market

m = Market()

class Portfolio:
    def __init__(self, holdings, cash):
        self.holdings = holdings    # List of tuples (name, qty)
        self.cash = cash            # Integer balance of cash

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
        for x in enumerate(self.holdings):
            index = x[0]
            holding = x[1]
            if stock_name in holding:
                new_quantity = holding[1] - quantity
                total = m.get_stock(stock_name).price * quantity
                if new_quantity >= 0:
                    if (new_quantity == 0):
                        self.holdings.pop(index)
                    else:
                        self.holdings[index] = (stock_name, new_quantity)
                    self.cash += total
                    return True
        return False

    def __repr__(self):
        print("Holdings:")
        for stock in self.holdings:
            print(stock[1], "shares of", stock[0])
        
        print("Cash:", self.cash)