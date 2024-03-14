import pandas as pd

class Optimiser:

    def __init__(self, period, tickers):
        self.period = period
        self.tickers = tickers

    #Creating a property-based attribute for stocks, has to contain more than 2 stocks
    @property
    def tickers(self):
        return self._tickers
    
    @tickers.setter
    def tickers(self, value):
        if len(value) < 2:
            raise ValueError("At least 2 stocks need to be selected")
        self._tickers = value

    def Portfolio(self):
        df = pd.read_csv("sp500_stocks_2019onwards")
        
        