

class Portfolio:
    def __init__(self, holdings, cash, market):
        self.holdings = holdings    # List of tuples (name, qty)
        self.cash = cash            # Integer balance of cash
        self.market = market

    def buy(self, stock_name, quantity):
        stock = self.market.get_stock(stock_name)
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
                total = self.market.get_stock(stock_name).price * quantity
                if new_quantity >= 0:
                    if (new_quantity == 0):
                        self.holdings.pop(index)
                    else:
                        self.holdings[index] = (stock_name, new_quantity)
                    self.cash += total
                    return True
        return False

    def __repr__(self):
        market_balance = 0
        print("--------------")
        print("# Your holdings:")
        for stock in self.holdings:
            stock_name = stock[0]
            quantity = stock[1]
            price = self.market.get_stock(stock_name).price
            market_balance += price * quantity
            if quantity == 1: print("  ", quantity, "share of", stock_name, "at", price)
            else: print("  ", quantity, "shares of", stock_name, "at", price)
        print()
        print("# Your market balance:", market_balance)
        print()
        print("# Your cash balance:", self.cash)
        print("--------------")
        print()