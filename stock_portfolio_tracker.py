

from alpha_vantage.timeseries import TimeSeries

# replace the key with your own alphavantage API key while running the application
ALPHA_VANTAGE_API_KEY = 'OZ2Q6AHWGQWS32U2'          # Key may vary according to the user.
class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            if quantity >= self.portfolio[symbol]:
                del self.portfolio[symbol]
            else:
                self.portfolio[symbol] -= quantity

    def get_portfolio_value(self):
        ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')
        total_value = 0
        for symbol, quantity in self.portfolio.items():
            try:
                data, _ = ts.get_quote_endpoint(symbol)
                price = float(data.iloc[0]['05. price'])  # Current price
                total_value += price * quantity
            except Exception as e:
                print(f"Error fetching data for {symbol}: {e}")
        return total_value

    def display_portfolio(self):
        print("Stock Portfolio:")
        for symbol, quantity in self.portfolio.items():
            print(f"{symbol}: {quantity} shares")

# Example usage:
portfolio = StockPortfolio()
portfolio.add_stock('AAPL', 10)
portfolio.add_stock('GOOGL', 5)
portfolio.add_stock('NVDA',2)
portfolio.remove_stock('NVDA',1)
portfolio.remove_stock('AAPL',5)

portfolio.display_portfolio()
print("Total Portfolio Value:", portfolio.get_portfolio_value())
