from market import Market
from portfolio import Portfolio

running = True

NASDAQ = Market()
p = Portfolio([], 10000, NASDAQ)

class Menu:
    def __init__(self):
        pass

    def __repr__(self):
        print("# Menu")
        print("1. Buy", "2. Sell", "3. Wait", "4. Exit")
        choice = int(input())
        if (choice == 1):
            print("What stock would you like to buy?")
            NASDAQ.__repr__()
            stock_name = input()
            print("How many shares?")
            quantity = int(input())
            p.buy(stock_name, quantity)
        elif (choice == 2):
            print("What stock would you like to sell?")
            stock_name = input()
            print("How many shares?")
            quantity = int(input())
            p.sell(stock_name, quantity)
        elif (choice == 4):
            global running
            running = False
        else:
            pass

menu = Menu()

if __name__ == "__main__":
    while(running):
        NASDAQ.update()
        p.__repr__()
        menu.__repr__()
