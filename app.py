from flask import Flask, render_template, request
from datetime import datetime, timedelta
from scipy.optimize import minimize
import numpy as np
import pandas as pd
import yfinance as yf
from fredapi import Fred
import os
from dotenv import load_dotenv
import helpers
import sp500tickers
import re

load_dotenv()
FRED_KEY = os.getenv('FRED_KEY')

app = Flask(__name__)

@app.route("/")
def form_page():
    tickers = ["(\"" + i + "\") " + j for i,j in sp500tickers.tickers_dict.items()]
    return render_template("index.html", tickers=tickers)

@app.route("/", methods=['POST'])
def optimise_portfolio():
    selected_tickers = request.form.getlist('ticker[]')
    selected_tickers = [re.findall('"([^"]*)"', s)[0] for s in selected_tickers if s != '']
    tickers = ["(\"" + i + "\") " + j for i,j in sp500tickers.tickers_dict.items()]
    if len(selected_tickers) < 2:
        error = 'At least 2 tickers need to be selected'
        return render_template('index.html', error=error, tickers=tickers)  

    end_date = datetime.today()
    start_date = end_date - timedelta(days = 5 * 365)

    # Getting stock prices from YFinance
    adj_close_df = yf.download(selected_tickers, start=start_date, end=end_date, ignore_tz=True)['Adj Close']

    # Calculate compounding returns 
    log_returns = np.log(adj_close_df/adj_close_df.shift(1))
    log_returns = log_returns.dropna()

    #Calculate covariance matrix, and annualising daily data by multiplying by 252 trading days
    cov_matrix = log_returns.cov()*252
    print(log_returns)

    # Getting risk-free return based on 10-year Treasury bills
    # fred = Fred(api_key=FRED_KEY)
    # ten_year_treasury_rate = fred.get_series_latest_release('GS10')/100
    # risk_free_rate = ten_year_treasury_rate.iloc[-1]
    risk_free_rate = 0.0413

    #Priming the parameters for calculation
    constraints = {'type': 'eq', 'fun': lambda weights: np.sum(weights)-1}
    bounds = [(0,0.5) for _ in range(len(selected_tickers))]
    initial_weights = np.array([1/len(selected_tickers)]*len(selected_tickers))

    #Calculating optimal portfolio weights
    optimise_results = minimize(helpers.neg_sharpe_ratio, initial_weights, args=(log_returns, cov_matrix, risk_free_rate), method='SLSQP', constraints=constraints, bounds=bounds)
    optimal_weights = optimise_results.x

    #Calculating performance metrics based on optimal weights using helpers.py functions
    optimal_portfolio_return = helpers.expected_returns(optimal_weights, log_returns)
    optimal_portfolio_volatility = helpers.standard_deviation(optimal_weights, cov_matrix)
    optimal_sharpe_ratio = helpers.sharpe_ratio(optimal_weights, log_returns, cov_matrix, risk_free_rate)

    return render_template('index.html', optimal_weights=zip(range(len(selected_tickers)), selected_tickers, optimal_weights), optimal_portfolio_return=optimal_portfolio_return, optimal_portfolio_volatility=optimal_portfolio_volatility, optimal_sharpe_ratio=optimal_sharpe_ratio, tickers=tickers)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
