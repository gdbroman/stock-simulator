from portfolio import Portfolio

p = Portfolio([], 1000)

if __name__ == "__main__":
    p.buy("TSLA", 2)
    p.__repr__()
    print(p.sell("TSLA", 1))