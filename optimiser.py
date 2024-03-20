import pandas as pd
import numpy as np
from scipy.optimize import minimize
from datetime import datetime, timedelta

class Optimiser:

    def __init__(self, period, tickers):
        self.period = period
        self.tickers = tickers

        self.optimal_weights = self.__portfolio()
        self.volatility = self.__volatility(self.optimal_weights,self.cov_matrix)
        self.expected_returns = self.__expected_returns(self.optimal_weights, self.logreturns)
        self.sharpe = self.__sharpe_ratio(self.optimal_weights,self.logreturns, self.cov_matrix, self.risk_free_rate)

    #Creating a property-based attribute for stocks, has to contain more than 2 stocks
    @property
    def tickers(self):
        return self._tickers
    
    @tickers.setter
    def tickers(self, value):
        if len(value) < 2:
            raise ValueError("Tickers list has to have at least 2 stocks")
        self._tickers = value

    #Helper functions
    def __portfolio(self):
        df = pd.read_csv("sp500_stocks_2019onwards.csv")

        #filter df by selected tickers
        df = df[df["Symbol"].isin(self.tickers)]

        #setting df index to datetime of "Date" column
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.set_index("Date")
        df = pd.pivot_table(df, values="Adj Close", columns="Symbol",index="Date")

        #filter df by selected period, CURRENTLY PERIOD IS FIXED TO 2 YEARS
        end_date = datetime.today()
        start_date = end_date - timedelta(days = 2 * 365)
        df = df.loc[start_date:end_date]

        # Calculate compounding returns 
        log_returns = np.log(df/df.shift(1))
        log_returns = log_returns.dropna()
        self.logreturns = log_returns

        #Calculate covariance matrix, and annualising daily data by multiplying by 252 trading days
        self.cov_matrix = log_returns.cov()*252

        # Getting risk-free return based on 10-year Treasury bills
        # fred = Fred(api_key=FRED_KEY)
        # ten_year_treasury_rate = fred.get_series_latest_release('GS10')/100
        # risk_free_rate = ten_year_treasury_rate.iloc[-1]
        self.risk_free_rate = 0.0413

        #Priming the parameters for calculation
        constraints = {'type': 'eq', 'fun': lambda weights: np.sum(weights)-1}
        bounds = [(0,0.5) for _ in range(len(self.tickers))]
        initial_weights = np.array([1/len(self.tickers)]*len(self.tickers))

        #Calculating optimal portfolio weights
        optimise_results = minimize(self.__neg_sharpe_ratio, initial_weights, args=(log_returns, self.cov_matrix, self.risk_free_rate), method='SLSQP', constraints=constraints, bounds=bounds)
        optimal_weights = optimise_results.x
        
        return optimal_weights

    def __volatility (self, weights, cov_matrix):
        variance = weights.T @ cov_matrix @ weights
        return np.sqrt(variance)

    def __expected_returns (self, weights, log_returns):
        return np.sum(log_returns.mean()*weights)*252

    def __sharpe_ratio(self, weights, log_returns, cov_matrix, risk_free_rate):
        return(self.__expected_returns(weights, log_returns)- risk_free_rate) / self.__volatility(weights, cov_matrix)

    def __neg_sharpe_ratio(self, weights, log_returns, cov_matrix, risk_free_rate):
        return -self.__sharpe_ratio(weights, log_returns, cov_matrix, risk_free_rate)

tickers = ["AAPL","GOOG", "AMZN", "AMD","AIG","EL"]
optimised = Optimiser(True,tickers)
print((optimised.logreturns.mean()*optimised.optimal_weights)*252)